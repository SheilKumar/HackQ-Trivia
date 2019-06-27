# Creating a new search method
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import requests
import urllib

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


question1 = "Who is the NBA all time top scorer?"
answers1 = ["Lebron James", "Kareem Abdul Jabbar", "Kobe Bryant"]
print(question1)
question1_lower = question1.lower()
answers1  = list(dict.fromkeys(answers1))
print(answers1)
answer_count = {}
for ans in answers1:
    answer_count[ans] = 0
print(answer_count)

GOOGLE_URL = "https://www.google.com/search?q={}&ie=utf-8&oe=utf-8"
my_url = GOOGLE_URL.format(question1)
print(my_url)
req = requests.get(my_url)
page_soup = soup(req.content, 'html.parser')
results_req = page_soup.findAll('div', attrs = {'class': 'ZINbbc'})
links_req = []
for r in results_req:
    link = r.find('a', href = True)
    links_req.append(link)
print(links_req)

import re

to_remove = []
clean_links = []

for i,l in enumerate(links_req):
    clean = re.search('\/url\?q\=(.*)\&sa',l)
    # Anything that doesn't fit the above pattern will be removed
    if clean is None:
        to_remove.append(i)
        continue
    clean_links.append(clean.group(1))

print(links_req)
