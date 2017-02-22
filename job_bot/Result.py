# Result class
import time
from job_bot.helpers import *


class Result(object):

    def __init__(self, element, browser):

        # TODO: make this work for jobs w/ conditional
        self._browser = browser
        self._main_tab = self._browser.current_window_handle

        try:
            self.type = result_type(element)
        except:
            print_log("error determining result type")
            self.type = 'unknown'

        if self.type == 'Person':

            # select name element and name element text
            self.name_element = element.find_element_by_class_name("name")
            self.name = self.name_element.text

            # select company name / job title
            co_selector = "p[class*='subline-level-1']"
            self.company = element.find_element_by_css_selector(
                str(co_selector)).text

        if self.type == 'Job':

            # select name element and name element text
            self.name_element = element.find_element_by_class_name(
                "job-card__title-line")
            self.name = self.name_element.text

            self.company = element.find_element_by_class_name(
                "job-card__company-name").text

        else:
            print_log('error parsing')
            self.element = element
