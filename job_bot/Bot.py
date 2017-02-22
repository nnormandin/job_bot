# Bot class
import time, logging

# web interaction
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from bs4 import BeautifulSoup

# helper functions
from job_bot.helpers import *
from job_bot.Search import Search



class Bot(object):
	
	def __init__(self, email = None, pw = None):
		
		# set log
		logging.basicConfig(filename='bot.log', filemode='w', level=logging.DEBUG)

		# gather credentials
		if email is None:
			email = get_email()
		if pw is None:
			pw = get_pw()

		# open browser
		try:
			self._browser = webdriver.Firefox()
			self._browser.get('https://www.linkedin.com/uas/login')
		except:
			print("-- unable to initiate connection to LinkedIn")

		# authenticate
		email_element = self._browser.find_element_by_id("session_key-login")
		pw_element = self._browser.find_element_by_id("session_password-login")
		clever_type(email_element, email)
		clever_type(pw_element, pw)
		pw_element.submit()
		time.sleep(1.5)

		# empty list to store search objects
		self.searches = []

		# counter of searches conducted
		self._nsearches = 0

		# wait
		print("-- waiting for load")
		wait_load(self._browser)


	def search(self, text, people = True):

		print("-- searching for {}".format(text))


		# find the search element
		try:
			searchbar = self._browser.find_element_by_xpath("//form[@id='extended-nav-search']//input")
		except:
			try:
				searchbar = self._browser.find_element_by_xpath("//div[@class='keyword-search-form']//input")
			except:
				print('-- failed to find search bar!')
				return

		# enter search terms
		clever_type(searchbar, text, submit = True)
		print("-- waiting for load")
		time.sleep(1.5)
		wait_load(self._browser, timeout = 30)

		# nav to job or people results
		if people:
			category = "People"
			path = "//button[@data-control-name='vertical_nav_people_toggle']"
			self._browser.find_element_by_xpath(str(path)).click()
			print("-- navigating to {} results".format(category))
		else:
			category = "Jobs"
			path = "///button[@data-control-name='vertical_nav_jobs_toggle']"
			self._browser.find_element_by_xpath(str(path)).click()
			print("-- navigating to {} results".format(category))

		# increment number of searches conducted
		self._nsearches += 1

		# put most recent search at [0]
		self.searches.insert(0, Search(self._browser, text))

		# create or overwrite current_search parameter
		self.current_search = self.searches[0]



	def quit_bot(self):
		print("-- bot shutting down")
		self._browser.quit()