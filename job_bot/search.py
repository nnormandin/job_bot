# search class

class Search(object):

	def __init__(self, _browser):
		self._browser = _browser

	def result(self):
		path = "//div[@class='search-result__wrapper']"
		self.result = self._browser.find_elements_by_xpath(str(path))

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

		return(self.result)

