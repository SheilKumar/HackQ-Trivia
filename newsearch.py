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
print(req)
page_soup = soup(req.content, 'html.parser')
print(page_soup)
print(my_url)
