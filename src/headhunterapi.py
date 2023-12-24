from src.job import PlatformAPI
import requests


response = requests.get('https://api.superjob.ru/2.0/oauth2/access_token/?code=c907a&redirect_uri=http%3A%2F%2Fwww.example.ru&client_id=3268&client_secret=v3.r.138048477.6de1aba17d65bf750b53fab5cf4d74586d9eda45.c55d6cd1ef1cc9a18f7bbb00762048a749951856')
print(response)

get('https://api.superjob.ru/2.0/oauth2/password/?login=example&password=example_password&client_id=1&client_secret=yourAppSecretKey')

api = 'v3.r.138048477.6de1aba17d65bf750b53fab5cf4d74586d9eda45.c55d6cd1ef1cc9a18f7bbb00762048a749951856'
id = 3268



class HeadHunterAPI(PlatformAPI):

    def get_vacancies(self, vacancy):
        pass
