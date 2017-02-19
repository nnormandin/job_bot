# job_bot

project to automate some basic LinkedIn workflows via Python with the intent of finding interesting profiles and job opportunities. uses selenium web driver, obfuscates artificiality by generating random pauses between keystrokes and actions.


# functionality

you can save your email and password to text files locally (within the /job_bot directory) as 'email.txt' and 'pw.txt' to avoid being prompted each time you create a job_bot session object. 

```python
# import job_bot module
import job_bot as jb

# start a job_bot session with selenium
bot = jb.Session()

# start interacting
bot.search_linkedin('really cool jobs')

# more to follow
```

# todo

* conduct sequence of searches given list of search terms
* view profiles, record name and occupation in log
* view jobs
* random scrolling
