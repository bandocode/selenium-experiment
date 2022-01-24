#!/usr/bin/env python3

from selenium import webdriver
from functools import cache
from global_vars import *
import argparse

def main():

	# Arguments for when you execute the file
	parser = argparse.ArgumentParser(description='Automatically answer questions on smartrevise.online')
	parser.add_argument('-e', '--email', type=str, required=True, help='The email of your account on smartrevise.online')
	parser.add_argument('-p', '--password', type=str, required=True, help='The password of your account on smartrevise.online')
	parser.add_argument('-l', '--link', type=str, required=True, help='The number at the end of the link where you answer questions')
	parser.add_argument('-H', '--headless', type=bool, help='Run in headless mode? True/False')
	parser.add_argument('-L', '--limit', type=int, help='How many questions to answer?')
	args = parser.parse_args()

	# Attribute the arguments to corresponding variables
	browser.cred_email = args.email
	browser.cred_password = args.password
	bot.answering_page = f"https://smartrevise.online/student/revise/Question/{args.link}"
	bot.limit = args.limit

	if args.headless == True:
		browser.headless = True
		browser.restart()

	# Login to smartrevise
	browser.login()

	while True:
		
		# If an error occurs while the bot is working, it will simply restart the browser instead of crashing. It ensures stability.
		try:
			bot.answer_question(browser)
		except:
			browser.restart()
			browser.login()

if __name__ == "__main__":
	main()
