from abc import ABC, abstractmethod
import json


class PlatformAPI(ABC):
    @abstractmethod
    def get_jobs(self, search_query):
        """
        Абстрактный класс для получения основных характеристик вакансии
        :param search_query:
        :return:
        """
        pass


class Job:
    def __init__(self, title, link, description, requirements, salary):
        self.title = title
        self.link = link
        self.description = description
        self.requirements = requirements
        self.salary = salary
