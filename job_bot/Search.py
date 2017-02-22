# Search class
import time
import random
import logging
from job_bot.Result import Result
from job_bot.helpers import *
from job_bot.search_helpers import *


class Search(object):

    def __init__(self, _browser, text, people):

        # search term
        self.text = str(text)

        if people:
            self.type = 'People'
        else:
            self.type = 'Jobs'

        # browser attribute
        self._browser = _browser

        # delay
        time.sleep(1.5)

        # wait for load
        wait_load(self._browser)

        self.results = recalculate_results(self._browser)

        # print out
        print_log("located {} results".format(len(self.results)))

    def next_page(self):

        # click the next button
        self._browser.find_element_by_class_name("next").click()

        # print out
        print_log("navigating to next page")

        # sleep
        time.sleep(1.5)

        # wait for load
        wait_load(self._browser)

        self.results = recalculate_results(self._browser)

    def visit(self, delay=5, idx=None):
        if not self.results:
            print_log("no results found")
            return

        if idx == None:
            idx = random.randrange(0, len(self.results) - 1)

        u = self.results[idx]
        u.name_element.click()
        print_log("viewing {0} ({1})".format(u.name, u.company))
        # print_log("{}".format(u.company))
        wait_load(self._browser)
        time.sleep(delay)
        page_back(self._browser)
        time.sleep(1)
        wait_load(self._browser)
        self.results = recalculate_results(self._browser)

    def recalculate(self):
        wait_load(self._browser)
        print_log('recalculating search results')

        if self.type.lower() not in self._browser.current_url:
            if self.type == 'People':
                people = True
            else:
                people = False

            search_category(self._browser, people)
            time.sleep(1)
            wait_load(self._browser)

        self.results = recalculate_results(self._browser)

        # todo:
        # 	Result class provides necessary functions / attributes
        # 		open in new tab
        # 		scroll on page
