from selenium import webdriver
from browser import Browser
from global_vars import *
from functools import cache
import os
import hashlib
import time
import json
import random

class answer_object(object):
	def __init__(self):

		# Variables
		self.restart_count = 0
		self.question_tracker = 0
		self.question_answering_delay = 5
		self.answer_gathering_delay = 2.5
		self.answering_page = "https://smartrevise.online/student/revise/Question/26"
		self.hashes = []
		self.answer_buttons = []
		self.answers_in_page = []
		self.question_hash = ""
		self.dat_question_hashes = []
		self.has_dat_file_been_updated = True
		self.limit = 6942021024

	def read_file(self):
		
		# Read the contents of the dat file and add them to the self.hashes array
		try:
			with open(os.getcwd()+"/dat", 'r') as data:
				self.hashes = data.read()
				self.hashes = json.loads(self.hashes)
		except:
			open(os.getcwd()+"/dat", 'w')

		for j in self.hashes:
			self.dat_question_hashes.append(j[0])

		# Once the arrays have been updated, we set this bool to false so that we dont constantly update
		# the arrays.
		self.has_dat_file_been_updated = False

	def update_hashes(self):

		# Writes the updated self.hashes list to the dat file
		with open(os.getcwd()+"/dat", 'w') as data:
			json_string = json.dumps(self.hashes, ensure_ascii=False)
			data.write(json_string)

		self.has_dat_file_been_updated = True

	def get_data_from_page(self, browser):

		# Searches for the web page element containing the question text and stores its hash in a variable
		self.question_hash = hashlib.sha256(browser.driver.find_element_by_xpath('//*[@id="questiontext"]').text.encode('utf-8')).hexdigest()

		# Loops through all the answer buttons and stores their hashes in an array
		self.answers_in_page = []
		for i in range(1,5): 
			self.answers_in_page.append(hashlib.sha256(browser.driver.find_element_by_xpath(f"/html/body/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[4]/div[{i}]/a/div/div[2]").text.encode('utf-8')).hexdigest())

	def get_correct_answer(self, browser):

		self.question_tracker += 1

		# Click the I don't know button
		browser.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[4]/div[5]/a/div/div[2]').click()

		self.answer_gathering_delay = random.randint(5,15)
		time.sleep(self.answer_gathering_delay)

		#We loop through all the buttons and we find the one with a different color than blue (that is the correct answer)
		for buttons in range(1,5): 
			if browser.driver.find_element_by_xpath(f"/html/body/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[4]/div[{buttons}]/a").value_of_css_property('background-color') != "rgb(93, 120, 255)": 
				correct_answer_hash = hashlib.sha256(browser.driver.find_element_by_xpath(f"/html/body/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[4]/div[{buttons}]/a/div/div[2]").text.encode('utf-8')).hexdigest()
				break
				
		return correct_answer_hash

	def click_correct_button(self, browser, ans):

		self.question_answering_delay = random.randint(5,15)
		print(f'Delay set to {self.question_answering_delay} seconds.')
		time.sleep(self.question_answering_delay)

		# Loop through every answer button and see which one matches with our potential answer
		for i in range(1,5):
			if hashlib.sha256(browser.driver.find_element_by_xpath(f"/html/body/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[4]/div[{i}]/a/div/div[2]").text.encode('utf-8')).hexdigest() == ans:
				browser.driver.find_element_by_xpath(f"/html/body/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[4]/div[{i}]/a/div/div[2]").click()
				self.question_tracker += 1
				break
		time.sleep(1.5)


	def answer_question(self, browser):

		# Restart every 60 questions answered.
		if self.question_tracker == self.limit:
			#browser.restart()
			#browser.login()
			#self.question_tracker = 0
			exit()


		# If the dat file has been changed, then we update the self.hashes list
		if self.has_dat_file_been_updated == True:
			self.read_file()

		# Go to the answering page
		browser.driver.get(self.answering_page)

		# Bool  used to determine whether or not the question was able to be answered
		answered = False

		# Get the question and answers from the webpage
		self.get_data_from_page(browser)

		# Cycle through every hash until it finds the one with the corresponding question and answers
		for obj in self.hashes:
	
			if obj[0] == self.question_hash:

				for ans in obj[1]:

					for j in range(0, len(self.answers_in_page)):

						if self.answers_in_page[j] == ans:

							self.click_correct_button(browser,ans)
							answered = True
							time.sleep(0.4)

		# If we failed to answer the question previously, we call the get_correct_answer() method 
		if answered == False:

			correct_answer = self.get_correct_answer(browser)

			# If the question is not in the dat file
			if self.question_hash not in self.dat_question_hashes: 

				# Add the question hash and the corresponding hashes to the list
				self.hashes.append([self.question_hash,[correct_answer]])

				#Apply the changes to the dat file
				self.update_hashes()

			else:

				for obj in self.hashes:

					# Find where the question hash is in the hash list
					if obj[0] == self.question_hash:

						# Add the correct answer to the hash list
						obj[1].append(correct_answer)

						#Apply the changes to the dat file.
						self.update_hashes()


			





