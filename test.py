import job_bot
import random

print('-- importing')

b = job_bot.Bot()

search_terms = ['quantitative', 'capital', 'analytics', 'neural networks', 'machine learning']
idx = random.randrange(0, len(search_terms)-1)

b.search(search_terms[idx])
b.current_search.visit()
b.current_search.visit()

b.current_search.next_page()
b.current_search.visit()
