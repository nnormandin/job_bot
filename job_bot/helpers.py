# base modules
import os
import time
import re
import logging
import urllib
import random
import getpass

# web interaction
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

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


def clever_type(element, text, submit=False):
    element.clear()
    for c in text:
        element.send_keys(str(c))
        time.sleep(random.uniform(0.03, 0.09))
    if submit:
        element.send_keys(Keys.RETURN)

# wait for browser to load


def wait_load(browser, timeout=20, elementID="nav-settings__dropdown-trigger"):
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

    elements = people_results + job_results

    return(elements)


def open_new_tab(browser, element):
    element.send_keys(Keys.CONTROL + Keys.RETURN)
    browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)


def close_tab(browser):
    browser.find_element_by_tag_name('body').send_keys(Keys.CONTORL + 'w')

# def select_main_tab(browser, main_tab):


def print_log(event):
    logging.info(str(event))
    print('-- {}'.format(event))


def page_back(browser):
    browser.execute_script("window.history.go(-1)")


def reload_page(browser):
    body = browser.find_element_by_tag_name("body")
    body.send_keys(Keys.CONTROL + 'r')


def result_type(element):
    try:
        element.find_element_by_class_name("name")
    except NoSuchElementException:
        return('Job')
    return('Person')


def find_next(browser):
    try:
        element.find_element_by_class_name("next")
    except:
        return(True)
    return(False)


def scroll_bottom(browser):
    y = 0

    while find_next(browser):
        browser.execute_script('window.scrollTo(0, {});'.format(y))
        y += 20
        if y > 6000:
            return
    wait_load(browser)
