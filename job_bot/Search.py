# Search class

from job_bot.Result import Result

class Search(object):

	def __init__(self, _browser):
		self._browser = _browser

		people_path = "//div[@class='search-result__wrapper']"
		job_path = "//div[@class='job-card__content-wrapper']"
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

		if elements:
			for i in elements:
				out.append(Result(i))
			

		self.results = out

		#todo:
			# move result function to init
			# Search.results object is list of results
			# Result class provides necessary functions / attributes
				# Result.name
				# Result.company
				# Result.link
				# open in new tab
				# scroll on page
				# record name and occupation to log file

		#return(self.results)

