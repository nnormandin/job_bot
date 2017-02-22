# imports
from job_bot.Result import Result
from job_bot.helpers import *


# refresh stale elements in DOM
def recalculate_results(browser):

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
				print("-- error occurred")

	return(out)

def search_category(browser, people = True):
		
		# nav to job or people results
		if people:
			category = 'People'
			path = "//button[@data-control-name='vertical_nav_people_toggle']"
			browser.find_element_by_xpath(str(path)).click()
			print_log("navigating to {} results".format(category))
		else:
			category = 'Jobs'
			path = "//button[@data-control-name='vertical_nav_jobs_toggle']"
			browser.find_element_by_xpath(str(path)).click()
			print_log("navigating to {} results".format(category))