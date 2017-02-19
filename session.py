# base libraries
import os, time, re
import urllib, random, getpass

# web interaction
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# helper functions
from helpers import clever_type
from helpers import get_email
from helpers import get_pw

class Session(object):
	
	def __init__(self, email = None, pw = None):
		
		# gather credentials
		if email is None:
			email = get_email()
		if pw is None:
			pw = get_pw()

		# open browser
		self._browser = webdriver.Firefox()
		self._browser.get('https://www.linkedin.com/uas/login')

		# authenticate
		email_element = self._browser.find_element_by_id("session_key-login")
		pw_element = self._browser.find_element_by_id("session_password-login")
		clever_type(email_element, email)
		clever_type(pw_element, pw)
		pw_element.submit()

		# wait
		search_button = "nav-settings__dropdown-trigger"
		wait = WebDriverWait(self._browser, 10)
		element = wait.until(EC.element_to_be_clickable((By.ID, str(search_button))))


	def search_linkedin(self, text):

		# find the search element
		try:
			searchbar = self._browser.find_element_by_xpath("//form[@id='extended-nav-search']//input")
		except:
			try:
				searchbar = self._browser.find_element_by_xpath("//div[@class='keyword-search-form']//input")
			except:
				print('failed to find search bar!')
				return

		# enter search terms
		clever_type(searchbar, text, submit = True)

		search_button = "nav-settings__dropdown-trigger"
		wait = WebDriverWait(self._browser, 10)
		element = wait.until(EC.element_to_be_clickable(By.ID, str(search_button)))

	def quit_bot(self):
		self._browser.quit()

if __name__ == '__main__':
	bot = Session()
	bot.search_linkedin('test test test')
	bot.quit_bot()