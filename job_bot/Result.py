# Result class

class Result(object):

	def __init__(self, element):
		name_element = element.find_element_by_class_name("name")
		self.name = name_element.text
		selector = "p[class*='subline-level-1']"
		self.company = element.find_element_by_css_selector(str(selector)).text
		

		#self.link = 
