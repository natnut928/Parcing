import requests
from datetime import date
from pprint import pprint
from lxml import html
import pandas as pd
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['news']
collection = db['yandex_news']

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

url = 'https://yandex.ru/news'

response = requests.get(url, headers=headers)

dom = html.fromstring(response.text)

items = dom.xpath('//article')

for item in items:
    pos = {}
    name = item.xpath('.//div[@class ="mg-card__annotation"]/text()')[0]
    link = item.xpath('.//a[@class ="mg-card__link"]/@href')[0]
    source = item.xpath('.//a[@class ="mg-card__source-link"]/text()')[0]
    time = item.xpath('.//span[@class ="mg-card-source_-time"]/text()')
    time = f"{date.today()}{time}"

    pos["News"] = name
    pos["Link"] = link
    pos["Time"] = time
    pos["Source"] = source
    pos["News_url"] = url

    if not collection.find_one({'Link' : pos['Link']}):
        collection.insert_one(pos)
