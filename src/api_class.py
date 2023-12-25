import os
from abc import ABC, abstractmethod

import requests
from dotenv import load_dotenv

load_dotenv()


class AbstractAPI(ABC):
    @abstractmethod
    def get_vacancies(self, vacancy):
        """
        Абстрактный класс для поиска вакансий через API
        :param vacancy: Запрос вакансии
        :return: список вакансий
        """
        pass


class HeadHunterAPI(AbstractAPI):
    def __init__(self):
        """
        Конструктор класса HeadHunterAPI.
        Устанавливает базовый URL и заголовки для запросов к API HeadHunter.
        """
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                      ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    def get_vacancies(self, vacancy):

        params = {"text": vacancy}
        response = requests.get(self.url, headers=self.headers, params=params)

        if response.status_code == 200:
            return response.json().get("items", [])
        else:
            print(f"'Ошибка при обращении к API:', {response.status_code}")
            return []


class SuperJobAPI(AbstractAPI):
    def __init__(self):
        """
        Конструктор класса SuperJobAPI.
        Устанавливает базовый URL, API-ключ и заголовки для запросов к API SuperJob.
        """
        self.url = "https://api.superjob.ru/2.0/vacancies"
        self.api_key = os.getenv("API_SUPERJOB")
        self.headers = {"X-Api-App-Id": self.api_key}

    def get_vacancies(self, vacancy):

        params = {"keyword": vacancy}
        response = requests.get(self.url, headers=self.headers, params=params)

        if response.status_code == 200:
            return response.json().get("objects", [])
        else:
            print(f"'Ошибка при обращении к API:', {response.status_code}")
            return []
