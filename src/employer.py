import requests

response = requests.get('https://api.hh.ru/')
print(response.text)

