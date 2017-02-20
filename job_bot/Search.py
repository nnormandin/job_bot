# search class

class Search(object):

	def __init__(self, _browser):
		self._browser = _browser

		path = "//div[@class='search-result__wrapper']"
		results = self._browser.find_elements_by_xpath(str(path))
		out = []
		for i in results:
			

		self.results = self._browser.find_elements_by_xpath(str(path))

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

		return(self.results)

