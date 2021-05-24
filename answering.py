from selenium import webdriver
from browser import Browser
from global_vars import *
from functools import cache
import os
import hashlib
import time
import json

class answer_object(object):
	def __init__(self):

		# Variables
		self.restart_count = 0
		self.question_tracker = 0
		self.question_answering_delay = 2.875
		self.answer_gathering_delay = 2.5
		self.answering_page = "https://smartrevise.online/student/revise/Question/26"
		self.hashes = []
		self.answer_buttons = []
		self.answers_in_page = []
		self.question_hash = ""
		self.dat_question_hashes = []
		self.has_dat_file_been_updated = True


	
	

			





