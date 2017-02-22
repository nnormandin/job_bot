# Search class
import time, random, logging
from job_bot.Result import Result
from job_bot.helpers import *
from job_bot.search_helpers import recalculate_results


class Search(object):

	def __init__(self, _browser, text):

		# search term
		self.search_term = str(text)

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

	def visit(self, delay = 5, idx = None):
		if not self.results:
			print("-- no results found")
			return

		if idx == None:
			idx = random.randrange(0, len(self.results)-1)

		u = self.results[idx]
		u.name_element.click()
		print_log("viewing {}".format(u.name))
		print_log("-- {}".format(u.company))
		wait_load(self._browser)
		time.sleep(delay)
		page_back(self._browser)
		time.sleep(1)
		wait_load(self._browser)
		self.results = recalculate_results(self._browser)

	def recalculate(self):
		wait_load(self._browser)
		print('-- recalculating search results')
		self.results = recalculate_results(self._browser)

		# todo:
		# 	Result class provides necessary functions / attributes
		# 		open in new tab
		# 		scroll on page
		# 		record name and occupation to log file

		#return(self.results)

