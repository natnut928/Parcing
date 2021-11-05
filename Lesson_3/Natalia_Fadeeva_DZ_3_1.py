import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from pprint import pprint
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError as dk

client = MongoClient('127.0.0.1', 27017)
db = client['hh_vacancy']
collection_db = db.vacancy

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

url = 'https://hh.ru/'

vacancy = input('Введите название вакансии: ')
pages = int(input('Сколько страниц отобразить: '))

params = {'clasters': 'true',
          'area': '1',
          'ored_clusters': 'true',
          'enable_snippets': 'true',
          'salary': None,
          'text': vacancy,
          'page': 0}

vacancy_list = {}

while params['page'] < pages:
    response = requests.get(url + 'search/vacancy/', params=params, headers=headers)
    dom = bs(response.text, 'html.parser')
    vacancies = dom.find_all('div', {'class': 'vacancy-serp-item'})

    if response.ok and vacancies:
        for vacancy in vacancies:
            vacancy_data = {}
            info = vacancy.find('a', {'class': 'bloko-link'})
            name = info.text
            link = info['href']
            site = url
            try:
                salary = vacancy.find('div', {'class': 'vacancy-serp-item__sidebar'}).text.split()
                if salary[0] == "до":
                    salary_min = None
                    salary_max = int(salary[1] + salary[2])
                    salary_currency = salary[3]
                elif salary[0] == "от":
                    salary_min = int(salary[1] + salary[2])
                    salary_max = None
                    salary_currency = salary[3]
                else:
                    salary_min = int(salary[0] + salary[1])
                    salary_max = int(salary[3] + salary[4])
                    salary_currency = salary[5]
            except:
                salary_min = None
                salary_max = None
                salary_currency = None

            vacancy_data['_id'] = name + link + site
            vacancy_data['name'] = name
            vacancy_data['link'] = link
            vacancy_data['site'] = site
            vacancy_data['salary_min'] = salary_min
            vacancy_data['salary_max'] = salary_max
            vacancy_data['salary_currency'] = salary_currency
            # vacancy_list.append(vacancy_data)

            if not collection_db.find_one({'link': vacancy_data['link']}):
                collection_db.insert_one(vacancy_data)

        print(f"Обработана {params['page'] + 1} страница ")
        params['page'] += 1
    else:
        break

#pprint(vacancy_list)

# df = pd.DataFrame(vacancy_list)
# df.to_csv('vacancy_list.csv', sep=',', encoding='utf-8')
print('Done')
