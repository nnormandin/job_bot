# search class

class Search(object):

	def __init__(self, _browser):
		self._browser = _browser

	def result(self):
		path = "//div[@class='search-result__wrapper']"
		self.result = self._browser.find_elements_by_xpath(str(path))
		return(self.result)

	