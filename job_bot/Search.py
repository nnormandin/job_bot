# Search class
import time
from job_bot.Result import Result
from job_bot.helpers import wait_a_minute, search_results


class Search(object):

	def __init__(self, _browser):

		# browser attribute
		self._browser = _browser

		# sleep
		time.sleep(1.5)

		# wait for load
		wait_a_minute(self._browser)
		

		out = search_results(self._browser)
			
		self.results = out

		# print out
		print("-- located {} results".format(len(self.results)))


	def next_page(self):

		# click the next button
		self._browser.find_element_by_class_name("next").click()

		# sleep
		time.sleep(1.5)

		# wait for load
		wait_a_minute(self._browser)


		out = search_results(self._browser)
			
		self.results = out		

		# todo:
		# 	move result function to init
		# 	Search.results object is list of results
		# 	Result class provides necessary functions / attributes
		# 		Result.name
		# 		Result.company
		# 		Result.link
		# 		open in new tab
		# 		scroll on page
		# 		record name and occupation to log file

		#return(self.results)

