import requests
from bs4 import BeautifulSoup as bs


url = input("Please put the URL: ")

# Bunch of articles I can scrape in these comments below
# https://www.cnn.com/2020/05/24/us/missouri-hairstylists-coronavirus-clients-trnd/index.html
# https://www.cnn.com/2018/02/14/health/ultra-processed-foods-cancer-study/index.html
# https://www.cnn.com/2020/05/24/health/us-coronavirus-sunday/index.html


page = requests.get(url)

soup = bs(page.content, 'html.parser')
results = soup.find_all('div', class_ = 'zn-body__paragraph')
if (results == None):
    print("NONE")
for r in results:
    text = r.text.strip()
    if (len(text) == 0):
        continue
    print(text, end = '\n\n')
