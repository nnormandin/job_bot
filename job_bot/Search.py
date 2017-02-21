# Search class
import time
from job_bot.Result import Result
from job_bot.helpers import *


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
		
		out = []
		elements = search_results(self._browser)

		if elements:
			for i in elements:
				try:
					out.append(Result(i, self._browser))
				except:
					print("-- error occurred")

		self.results = out

		# print out
		print("\n-- located {} results".format(len(self.results)))


	def next_page(self):

		# click the next button
		self._browser.find_element_by_class_name("next").click()

		# print out
		print("\n-- navigating to next page")

		# sleep
		time.sleep(1.5)

		# wait for load
		wait_load(self._browser)

		out = []
		elements = search_results(self._browser)

		if elements:
			for i in elements:
				try:
					out.append(Result(i, self._browser))
				except:
					print("-- error occurred")

		self.results = out

		# todo:
		# 	Result class provides necessary functions / attributes
		# 		Result.name
		# 		Result.company
		# 		Result.link
		# 		open in new tab
		# 		scroll on page
		# 		record name and occupation to log file

		#return(self.results)

