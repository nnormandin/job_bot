# basic utilities

# import main libraries
import os, time, re
import urllib, random, getpass

# web interaction
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# find email or ask for it
def get_email():
	if 'email.txt' in os.listdir():
		print('email located in directory\n')
		email = open('email.txt').read().strip()
	else:
		email = input('enter email: ')
	return(email)

# find pw or ask for it
def get_pw():
	if 'pw.txt' in os.listdir():
		print('pasword located in directory\n')
		pw = open('pw.txt').read().strip()
	else:
		pw = getpass.getpass('enter password: ')
	return(pw)

# by-character input with random sleep
def clever_type(element, text, submit = False):
    element.clear()
    for c in text:
        element.send_keys(str(c))
        time.sleep(random.uniform(0.05,0.15))
    if submit:
    	element.send_keys(Keys.RETURN)

# initiate session
def initiate_linkedin(email = None, pw = None):
	
	# gather credentials
	if email is None:
		email = get_email()
	if pw is None:
		pw = get_pw()

	# open browser and navigate to linkedin
	browser = webdriver.Firefox()
	browser.get('https://www.linkedin.com/uas/login')

	# authenticate
	email_element = browser.find_element_by_id("session_key-login")
	pw_element = browser.find_element_by_id("session_password-login")
	clever_type(email_element, email)
	clever_type(pw_element, pw, submit = True)
	return(browser)


# robust search utility
def search_linkedin(browser, text):

	# find the search element
	try:
		searchbar = browser.find_element_by_xpath("//form[@id='extended-nav-search']//input")
	except NoSuchElementException:
		try:
			searchbar = browser.find_element_by_xpath("//div[@class='keyword-search-form']//input")
		except NoSuchElementException:
			print('failed to find search bar!')
			return

	#return(searchbar)
	# enter search terms
	clever_type(searchbar, text, submit = True)

	# return search results

#def search_results():


