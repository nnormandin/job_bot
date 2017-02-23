import job_bot
import random

print('-- importing')

b = job_bot.Bot()

search_terms = ['quantitative', 'capital', 'analytics', 'neural networks', 'machine learning']
idx = random.randrange(0, len(search_terms)-1)

b.new_search(search_terms[idx], people = False)
b.search.visit()
b.search.visit()

b.search.next_page()
b.search.visit()

idx = random.randrange(0, len(search_terms)-1)
b.new_search(search_terms[idx], people = False)

