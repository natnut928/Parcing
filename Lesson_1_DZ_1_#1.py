import requests

#header = {
#    'USER-AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'
#}
from pprint import pprint
# Имя пользователя github
username = "natnut928"
# url для запроса
url = f"https://api.github.com/users/{username}"
# делаем запрос и возвращаем json
user_data = requests.get(url).json()
# довольно распечатать данные JSON
pprint(user_data)
