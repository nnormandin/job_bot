from job_bot.Result import Result
from job_bot.helpers import *


# refresh stale elements in DOM
def recalculate_results(browser):

	out = []

	
	elements = search_results(browser)

	if elements:
		for i in elements:
			try:
				out.append(Result(i, browser))
			except:
				print("-- error occurred")

	return(out)