import json
from abc import ABC, abstractmethod

from vacancy_ import Vacancy


class AbstractSaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        """
        Абстрактный класс, добавляющий вакансии в файл
        :param vacancy: Список вакансий
        :return bool:
        """
        pass

    @abstractmethod
    def get_vacancies_by_keywords(self, keywords):
        """
        Абстрактный метод для получения списка вакансий по ключевым словам.
        :param keywords: Ключевые слова фильтрации
        :return: Отфильтрованный список вакансий
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """
        Абстрактный метод для удаления вакансии из хранилища.
        :param vacancy: Вакансия для удаления
        :return bool: True, если удаление успешно
        """
        pass


class JSONSaver(AbstractSaver):
    def __init__(self, filename="vacancies.json"):
        self.filename = filename
        self.vacancies = []

    def add_vacancy(self, vacancy):
        self.vacancies.append(vars(vacancy))
        return True

    def get_vacancies_by_keywords(self, keywords):
        return [
            Vacancy(**vacancy)
            for vacancy in self.vacancies
            if all(vacancy.get(key) == value for key, value in keywords.items())
        ]

    def delete_vacancy(self, vacancy):
        vacancy_data = vars(vacancy)
        if vacancy_data in self.vacancies:
            self.vacancies.remove(vacancy_data)
            self.save_to_file()
            return True
        return False

    def save_to_file(self):
        with open(self.filename, "w", encoding='utf-8') as file:
            json.dump(self.vacancies, file, ensure_ascii=False)
