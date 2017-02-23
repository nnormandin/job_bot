# imports
import time
from job_bot.Result import Result
from job_bot.helpers import *


# refresh stale elements in DOM
def recalculate_results(browser, type, again=True):

    # empy list
    out = []

    # find all result elements in browser
    elements = search_results(browser)

    # instantiate Result type objects
    if elements:
        for i in elements:
            try:
                out.append(Result(i, browser))
            except:
                print_log("faulty element found")
                time.sleep(1)
                verify_category(browser, type)
                wait_load(browser)
                scroll_bottom(browser)

    if not out:
        if again:
            recalculate_results(browser, type=type, again=False)
            verify_category(browser, type)
            wait_load(browser)
            scroll_bottom(browser)

    return(out)


def search_category(browser, people=True):

        # nav to job or people results
    if people:
        category = 'People'
        path = "//button[@data-control-name='vertical_nav_people_toggle']"
        browser.find_element_by_xpath(str(path)).click()
        wait_load(browser)
        scroll_bottom(browser)
        print_log("navigating to {} results".format(category))
    else:
        category = 'Jobs'
        path = "//button[@data-control-name='vertical_nav_jobs_toggle']"
        browser.find_element_by_xpath(str(path)).click()
        wait_load(browser)
        scroll_bottom(browser)
        print_log("navigating to {} results".format(category))

# def load_search_terms(dir = None):


def verify_category(browser, type):
    if type not in browser.current_url:
        print_log("incorrect category located")
        return(False)
        if type == 'People':
            search_category(browser)
            wait_load(browser)
            scroll_bottom(browser)
        else:
            search_category(browser, people=False)
            wait_load(browser)
            scroll_bottom(browser)
    return(True)
