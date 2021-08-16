import requests
from lxml import html

# lenta

url_lenta = 'https://lenta.ru/'

xpath_title_lenta = '//*[@id="root"]/section[2]/div/div/div[1]/section[1]/div[2]/div[2]/a/text()'

xpath_date_lenta = '//*[@id="root"]/section[2]/div/div/div[1]/section[1]/div[2]/div[2]/a/time/text()'

xpath_link_lenta = '//*[@id="root"]/section[2]/div/div/div[1]/section[1]/div[2]/div[2]/a/@href'

response = requests.get(url_lenta)

root = html.fromstring(response.text)

#root.make_links_absolute(xpath_title_lenta)

print(root.xpath(xpath_date_lenta), root.xpath(xpath_title_lenta), root.xpath(xpath_link_lenta))

# mail

url_mail = 'https://news.mail.ru/'

xpath_title_mail = '//*[@id="index_page"]/div[7]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/span[2]/a/span/text()'

xpath_date_mail = '//*[@id="index_page"]/div[7]/div[2]/div[2]/div/div/div/div[1]/div/ul/li[1]/span/a/span/text'

xpath_link_mail = '//*[@id="index_page"]/div[7]/div[2]/div[2]/div/div/div/div[1]/div/ul/li[1]/span/a/href'

response = requests.get(url_mail)

root = html.fromstring(response.text)

print(root.xpath(xpath_date_mail), root.xpath(xpath_title_mail), root.xpath(xpath_link_mail))

# yandex

url_yandex = 'https://yandex.ru/news'

xpath_title_yandex = '//*[@id="neo-page"]/div/div[2]/div/div[1]/div[1]/div[3]/article/div[1]/div/div/text()'

xpath_date_yandex = '//*[@id="neo-page"]/div/div[2]/div/div[1]/div[1]/div[3]/article/div[3]/div[1]/div/span[2]/text()'

xpath_link_yandex = '//*[@id="neo-page"]/div/div[2]/div/div[1]/div[1]/div[3]/article/div[1]/div/a/@href'

response = requests.get(url_yandex)

root = html.fromstring(response.text)

print(root.xpath(xpath_date_yandex), root.xpath(xpath_title_yandex), root.xpath(xpath_link_yandex))
