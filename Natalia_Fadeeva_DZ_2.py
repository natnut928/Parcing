#from bs4 import BeautifulSoup
#from fake_headers import Headers
#import lxml
#import pandas as pd
import requests


count=10
url = 'https://api.hh.ru/vacancies?per_page=10&page=1&specialization=1&area=1&text=руководитель&currency=RUR&only_with_salary=true'
#headers = Headers(headers = True).generate()
response = requests.get(url)
r = response.json()
print(r)
#soup = BeautifulSoup(response.text, 'lxml')

with open('hh_vac.csv', 'w') as f:
    f.write(",Name, Min, Max, Position URL, Site\n")
    for i in range(10):
        rec = r["items"][i]
        s_min = rec["salary"]["from"]
        s_max = rec["salary"]["to"] if rec["salary"]["to"] else s_min

        f.write("{},{},{},{},{},{}\n".format(i,rec["name"],s_min,s_max, rec["alternate_url"], "http://hh.ru"))

        # print(rec["name"], s_min, s_max, rec["alternate_url"], "http://hh.ru")
print("we are done")
#df = pd.DataFrame(vacancies_info).to_csv('DZ_2.csv')