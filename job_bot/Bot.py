import time

# web interaction
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# helper functions
from job_bot.helpers import clever_type
from job_bot.helpers import get_email
from job_bot.helpers import get_pw
from job_bot.helpers import wait_a_minute
from job_bot.search import Search

class Bot(object):
	
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
		time.sleep(1.5)

		# wait
		print("-- waiting for load")
		wait_a_minute(self._browser)


	def search_linkedin(self, text, people = True):

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
		wait_a_minute(self._browser, timeout = 30)

		# nav to job or people results
		if people:
			path = "//button[@data-control-name='vertical_nav_people_toggle']"
			self._browser.find_element_by_xpath(str(path)).click()
			print("-- navigating to People results")
		else:
			path = "///button[@data-control-name='vertical_nav_companies_toggle']"
			self._browser.find_element_by_xpath(str(path)).click()
			print("-- navigating to Company results")

		return(Search(self._browser))

	def quit_bot(self):
		self._browser.quit()

if __name__ == '__main__':
	bot = Bot()
	bot.search_linkedin('test test test')
	bot.quit_bot()