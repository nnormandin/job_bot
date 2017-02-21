# base modules
import os, time, re
import urllib, random, getpass

# Result class
from job_bot.Result import Result

# web interaction
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# find email or ask for it
def get_email():
	if 'email.txt' in os.listdir():
		print('-- email located in directory')
		email = open('email.txt').read().strip()
	else:
		email = input('-- enter email: ')
	return(email)

# find pw or ask for it
def get_pw():
	if 'pw.txt' in os.listdir():
		print('-- password located in directory')
		pw = open('pw.txt').read().strip()
	else:
		pw = getpass.getpass('-- enter password: ')
	return(pw)

# by-character input with random sleep
def clever_type(element, text, submit = False):
    element.clear()
    for c in text:
        element.send_keys(str(c))
        time.sleep(random.uniform(0.03,0.09))
    if submit:
    	element.send_keys(Keys.RETURN)

# wait for browser to load
def wait_load(browser, timeout = 20, elementID = "nav-settings__dropdown-trigger"):
		time.sleep(0.5)
		wait = WebDriverWait(browser, timeout)
		element = wait.until(EC.element_to_be_clickable((By.ID, str(elementID))))

# convert search results to Result class
def search_results(browser):

	wait_load(browser)

	# search paths
	people_path = "//div[@class='search-result__wrapper']"
	job_path = "//div[@class='job-card__content-wrapper']"

	# find all search results
	try:
		people_results = browser.find_elements_by_xpath(str(people_path))
	except:
		print("-- no People found in search results")
	try:
		job_results = browser.find_elements_by_xpath(str(job_path))
	except:
		print("-- no Jobs found in search results")

	out = []
	elements = people_results + job_results

	# Result objects
	if elements:
		for i in elements:
			try:
				out.append(Result(i, browser))
			except:
				print("-- error occurred")

	return(out)


#def page_back(browser):

#def reload_page(browser):

#def rand_scroll(browser):