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

		# Constants
		self.min_delay_interval = 3
		self.max_delay_interval = 5

		# Nothing will happen if these are changed
		self.question_tracker = 0
		self.question_answering_delay = 0		
		self.answer_gathering_delay = 2.5
		self.limit = 666	

		# Algo-related variables
		self.answering_page = ""
		self.question_hash = ""
		self.answers_in_page = []
		self.update = True
		self.scraped_data = {}

	def read_file(self):
		
		try:
			with open(os.getcwd()+"/hash_table.json", 'r') as data:
				self.scraped_data = data.read()
				self.scraped_data = json.loads(self.scraped_data)
		except:
			open(os.getcwd()+"/hash_table.json ", 'w')

		self.update = False 
 
	def update_hashes(self):

		# Writes the updated self.hashes list to the dat file
		with open(os.getcwd()+"/hash_table.json", 'w') as data:
			json_string = json.dumps(self.scraped_data, ensure_ascii=False)
			data.write(json_string)

		self.update = True


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

		self.answer_gathering_delay = random.randint(self.min_delay_interval,self.max_delay_interval)
		time.sleep(self.answer_gathering_delay+2)

		#We loop through all the buttons and we find the one with a different color than blue (that is the correct answer)
		for buttons in range(1,5): 
			if browser.driver.find_element_by_xpath(f"/html/body/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[4]/div[{buttons}]/a").value_of_css_property('background-color') != "rgb(93, 120, 255)": 
				correct_answer_hash = hashlib.sha256(browser.driver.find_element_by_xpath(f"/html/body/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[4]/div[{buttons}]/a/div/div[2]").text.encode('utf-8')).hexdigest()
				break
		
		return correct_answer_hash

	def click_correct_button(self, browser, ans):

		self.question_answering_delay = random.randint(self.min_delay_interval,self.max_delay_interval)
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
		answered = False

		if self.question_tracker == self.limit:
			exit()

		# If the dat file has been changed, then we update the self.hashes list
		if self.update == True:
			self.read_file()

		# Go to the answering page
		browser.driver.get(self.answering_page)

		# Get the question and answers from the webpage
		self.get_data_from_page(browser)

		try:
			answers = self.scraped_data[f'{self.question_hash}'] 

			for k in answers:
				for m in self.answers_in_page:
					if k == m:
						self.click_correct_button(browser,k)
						answered = True
						time.sleep(0.4)

			if answered == False:

				self.scraped_data[f'{self.question_hash}'][1].append(self.get_correct_answer(browser))
				self.update_hashes()

		except:

			self.scraped_data[f'{self.question_hash}'] = [self.get_correct_answer(browser)]
			self.update_hashes()

			





