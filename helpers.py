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
		print('password located in directory\n')
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