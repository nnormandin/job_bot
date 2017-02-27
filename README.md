# job_bot

project to automate some basic LinkedIn workflows via Python with the intent of finding interesting profiles and job opportunities. uses selenium web driver, obfuscates artificiality by generating random pauses between keystrokes and actions.


# functionality

you can save your email and password to text files locally (within the /job_bot directory) as 'email.txt' and 'pw.txt' to avoid being prompted each time you create a job_bot session object. 

```python
# import job_bot module
import job_bot as jb

# start a job_bot session with selenium
bot = jb.Bot()

# search for something / someone / a job
bot.new_search('data scientist')

# visit the first profile in the search
bot.search.visit(0)

# or visit one of the results at random
bot.search.visit()

# see all of the results, and associated data
bot.search.results
bot.search.results[0].name
bot.search.results[0].company

# navigate to the next page
bot.search.next_page()

# go right into a new search
bot.new_search('something else')
bot.search.search_term
bot.search.visit()

# more to follow
```

# todo

* conduct sequence of searches given list of search terms
* random scrolling
* state transition probabilities
