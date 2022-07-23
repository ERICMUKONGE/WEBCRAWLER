from turtle import title
import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url ="https://jinja.palletsprojects.com/en/3.1.x/api/#high-level-api" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'class':'item-name'}):
            href = "https://jinja.palletsprojects.com" + link.get('href')
            title = link.string
            print(href)
            print(title)
        page += 1
trade_spider(1)            