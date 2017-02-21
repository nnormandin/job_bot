# job_bot

project to automate some basic LinkedIn workflows via Python with the intent of finding interesting profiles and job opportunities. uses selenium web driver, obfuscates artificiality by generating random pauses between keystrokes and actions.


# functionality

you can save your email and password to text files locally (within the /job_bot directory) as 'email.txt' and 'pw.txt' to avoid being prompted each time you create a job_bot session object. 

```python
# import job_bot module
import job_bot as jb

# start a job_bot session with selenium
bot = jb.Bot()

# use search method on Bot class object
search1 = bot.search_linkedin('really cool jobs')

# each Search class object stores results
len(search1.results)

# each result (either a person or a job listing) is a Result class object
search1[0].name
search1[0].company 

# more to follow
```

# todo

* conduct sequence of searches given list of search terms
* log name/company for jobs and people
* random scrolling
* state transition probabilities
