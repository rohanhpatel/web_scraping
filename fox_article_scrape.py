import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.foxnews.com/politics/gop-sues-california-newsom-vote-by-mail-order-illegal-power-grab-claim'
page = requests.get(url)

soup = bs(page.content, 'html.parser')
results = soup.find_all('p')
for r in results:
    text = r.text.strip()
    if (len(text) == 0):
        continue
    print(text, end = '\n\n')
