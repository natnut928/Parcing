import requests

headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                         'Version/14.1.1 Safari/605.1.15',

           'Authorization': 'Basic cG9zdG1hbjpwYXNzd29yZA=='}

req = requests.get('https://postman-echo.com/basic-auth', headers=headers)

print('Заголовки: \n',  req.headers)
print('Ответ: \n',  req.text)