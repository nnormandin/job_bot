import os, time, re
import urllib, random, getpass

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


def getEmail():
    email_verified = False
    while not email_verified:
        email = input('Linkedin Email: ')
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            email_verified = True
            return email
        else:
            print("Email not valid. Please try again")


def getPassword():
    pw_verified = False
    while not pw_verified:
        password = getpass.getpass('Password:')
        if len(password) >= 6:
            pw_verified = True
            return password
        else:
            print("Password must have 6 or more characters")


def getPeopleLinks(page):
    links = []
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            if 'profile/view?id' in url:
                links.append(url)
    return(links)


def getJobLinks(page):
    links = []
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            if '/jobs' in url:
                links.append(url)

    return(links)


def getID(url):
    pURL = urllib.parse.urlparse(url)
    return(urllib.parse.urlparse.parse_qs(pURL.query)['id'][0])()


def ViewBot(browser):
    visited = {}
    pList = []
    counter = 0

    while True:
        time.sleep(random.uniform(3.4, 9.5))
        page = BeautifulSoup(browser.page_source)
        people = getPeopleLinks(page)

        for person in people:
            ID = getID(person)
            if ID not in visited:
                pList.append(person)
                visited[ID] = 1

        if pList:
            person = pList.pop()
            browser.get(person)
            counter += 1


        else:
            jobs = getJobLinks(page)
            if jobs:
                job = random.choice(jobs)
                root = "http://www.linkedin.com"
                roots = "https://www.linkedin.com"

                if root not in job or roots not in job:
                    job = "https://www.linkedin.com" + job
                browser.get(job)

            else:
                print("I'm lost in this sea of jobs!!!")
                print("I'm giving up....")
                break

        print("[+] " + browser.title + " Visited!\n(" + str(counter)+"/" + str(len(pList)) + ") Visited/Queue")
        print(person)
        print("")

def Main():
    email = getEmail()
    password = getPassword()
    
    print('Logging in with %s' % email)
    browser = webdriver.Firefox()
    browser.get("https://www.linkedin.com/uas/login")

    emailElement = browser.find_element_by_id("session_key-login")
    emailElement.send_keys(email)
    passwordElement = browser.find_element_by_id("session_password-login")
    passwordElement.send_keys(password)
    passwordElement.submit()

    os.system('clear')
    print("[+] Success! You are now logged in with %s." % email)
    print("[+] The bot is starting!")
    ViewBot(browser)
    browser.close()


if __name__ == "__main__":
    email = open('email.txt').read().strip()
    pw = open('pw.txt').read().strip()
    browser = webdriver.Firefox()
    browser.get('https://www.linkedin.com/uas/login')

    emailElement = browser.find_element_by_id("session_key-login")
    emailElement.send_keys(email)
    passwordElement = browser.find_element_by_id("session_password-login")
    passwordElement.send_keys(pw)
    passwordElement.submit()


