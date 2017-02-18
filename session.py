class Session(object):
	
	def __init__(self, email = None, pw = None):
		
		# gather credentials
		if email is None:
			email = get_email()
		if pw is None:
			pw = get_pw()

		# open browser
		browser = webdriver.Firefox()
		browser.get('https://www.linkedin.com/uas/login')

		# authenticate
		email_element = browser.find_element_by_id("session_key-login")
		pw_element = browser.find_element_by_id("session_password-login")
		clever_type(email_element, email)
		clever_type(pw_element, pw, submit = True)

	def search_linkedin(browser, text):

		# find the search element
		try:
			searchbar = browser.find_element_by_xpath("//form[@id='extended-nav-search']//input")
		except NoSuchElementException:
			try:
				searchbar = browser.find_element_by_xpath("//div[@class='keyword-search-form']//input")
			except NoSuchElementException:
				print('failed to find search bar!')
				return

		#return(searchbar)
		# enter search terms
		clever_type(searchbar, text, submit = True)