# Search class
import time
from job_bot.Result import Result
from job_bot.helpers import wait_a_minute, search_results


class Search(object):

	def __init__(self, _browser):

		# browser attribute
		self._browser = _browser

		# wait for load
		wait_a_minute(self._browser)
		time.sleep(1.5)

		out = search_results(self._browser)
			
		self.results = out

		# print out
		print("-- located {} results".format(len(self.results)))


	def next_page(self):

		# click the next button
		self._browser.find_element_by_class_name("next").click()

		# wait for load
		wait_a_minute(self._browser)

		# search paths
		people_path = "//div[@class='search-result__wrapper']"
		job_path = "//div[@class='job-card__content-wrapper']"

		# find all search results
		try:
			people_results = self._browser.find_elements_by_xpath(str(people_path))
		except:
			print("-- no People found in search results")
		try:
			job_results = self._browser.find_elements_by_xpath(str(job_path))
		except:
			print("-- no Jobs found in search results")

		out = []
		elements = people_results + job_results

		# Result objects
		if elements:
			for i in elements:
				out.append(Result(i))
			
		self.results = out		

		todo:
			move result function to init
			Search.results object is list of results
			Result class provides necessary functions / attributes
				Result.name
				Result.company
				Result.link
				open in new tab
				scroll on page
				record name and occupation to log file

		return(self.results)

