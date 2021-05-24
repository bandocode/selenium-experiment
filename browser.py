from selenium import webdriver

class Browser(object):
	def __init__(self):

		# Variables used later to login into the website
		self.cred_email = 0
		self.cred_password = 0

		#Headless
		self.headless = False

		# Masking selenium to bypass the block against automated browsers
		options = webdriver.ChromeOptions()
		options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 11.2; rv:85.0) Gecko/20100101 smart-revise-bot /christ")
		options.add_argument('--disable-blink-features=AutomationControlled')

		# Launch the browser
		self.driver = webdriver.Chrome(options=options)

	def login(self):
		self.driver.get("https://smartrevise.online/Account/Login")
		self.driver.find_element_by_xpath('//*[@id="Email"]').send_keys(self.cred_email)
		self.driver.find_element_by_xpath('//*[@id="Password"]').send_keys(self.cred_password)
		self.driver.find_element_by_xpath('//*[@id="btnLogin"]').click()

	def restart(self):
		self.driver.quit()

		options = webdriver.ChromeOptions()
		if self.headless == True: options.add_argument('headless')
		options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 11.2; rv:85.0) Gecko/20100101 smart-revise-bot /christ")
		options.add_argument('--disable-blink-features=AutomationControlled')

		self.driver = webdriver.Chrome(options=options)

	def quit(self):
		self.driver.quit()


	