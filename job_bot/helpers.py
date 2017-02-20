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


def wait_a_minute(browser, timeout = 20, elementID = "nav-settings__dropdown-trigger"):
		wait = WebDriverWait(browser, timeout)
		element = wait.until(EC.element_to_be_clickable((By.ID, str(elementID))))