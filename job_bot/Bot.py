# Bot class
import time
import logging

# web interaction
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# helper functions
from job_bot.helpers import *
from job_bot.search_helpers import *
from job_bot.Search import Search


class Bot(object):

    def __init__(self, email=None, pw=None):

        # set log
        logging.basicConfig(filename='bot.log', level=logging.INFO)

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
            print_log("unable to initiate connection to LinkedIn")
            return

        print_log("job_bot session initiated")

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

    def new_search(self, text, people=True):

        print_log("searching for {}".format(text))

        # find the search element
        try:
            searchbar = self._browser.find_element_by_xpath(
                "//form[@id='extended-nav-search']//input")
        except:
            try:
                searchbar = self._browser.find_element_by_xpath(
                    "//div[@class='keyword-search-form']//input")
            except:
                print_log('failed to find search bar!')
                return

        # enter search terms
        clever_type(searchbar, text, submit=True)
        print("-- waiting for load")
        time.sleep(1.5)
        wait_load(self._browser, timeout=30)

        # nav to job or people results
        search_category(self._browser, people)
        scroll_bottom(self._browser)

        # increment number of searches conducted
        self._nsearches += 1

        # put most recent search at [0]
        self.searches.insert(0, Search(self._browser, text, people))

        # create or overwrite current_search parameter
        self.search = self.searches[0]

    # class teardown
    def quit_bot(self):
        print_log("bot shutting down")
        self._browser.quit()


# rework hierarchy:
# Bot
#   - browser
#   - new_search
#   - Search
#       type, enter, wait, select cat, wait, scroll down, scroll up
#       calculate results
#           - Results
#               click into new tab, switch tabs, {actions}, close tab, switch back