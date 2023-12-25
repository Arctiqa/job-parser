from src.job import PlatformAPI
import requests


response = requests.get('https://api.superjob.ru/2.0/oauth2/access_token/?code=c907a&redirect_uri=http%3A%2F%2Fwww.example.ru&client_id=3268&client_secret=v3.r.138048477.6de1aba17d65bf750b53fab5cf4d74586d9eda45.c55d6cd1ef1cc9a18f7bbb00762048a749951856')
print(response.text)

api = 'v3.r.138048477.6de1aba17d65bf750b53fab5cf4d74586d9eda45.c55d6cd1ef1cc9a18f7bbb00762048a749951856'
id = 3268

idhh = 104772957
response2 = requests.get('https://hh.ru/oauth/authorize?response_type=code&client_id=LOTHHN3BSET0I7IQNF3N5I0362AE1D14I6M74CAIQ5H49F7MT4PLMTVV7JTOA6QA')

headers = {
    'User-Agent': 'api-test-agent'
}

response2 = requests.get('https://api.hh.ru/vacancies', headers=headers, verify=True)

print(response2.json())

class HeadHunterAPI(PlatformAPI):

    def get_vacancies(self, vacancy):
        pass
