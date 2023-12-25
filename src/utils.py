from typing import List

from src.vacancy import Vacancy


def sort_vacancies(vacancies):
    """
    Сортирует вакансии по зарплате.
    :param vacancies: Список вакансий
    :return: Отсортированный список
    """
    return sorted(vacancies, key=lambda x: x.salary)


def get_top_n_vacancies(vacancies, n):
    """
    Возвращает первые n вакансий
    :param vacancies: Список вакансий
    :param n: Количество вакансий
    :return: Список из n вакансий
    """
    return vacancies[:n]


def vacancies_info(vacancies):
    """
    Выводит информацию о вакансиях в консоль.
    :param vacancies: Список вакансий
    :return: None
    """
    for i, vacancy in enumerate(vacancies, start=1):
        print(f"{i}. {vacancy.title} ({vacancy.salary}): {vacancy.link}")


def filter_vacancies(vacancies: List[Vacancy], filter_words: List[str]) -> List[Vacancy]:
    """
    Фильтрует вакансии по ключевым словам.
    :param vacancies: Список вакансий
    :param filter_words: Список ключевых слов для фильтрации
    :return: Отфильтрованный список
    """
    filtered_vacancies = []

    for vacancy in vacancies:
        # Проверяем, содержатся ли все ключевые слова в описании вакансии
        print(vacancy)
        # if all(word.lower() in vacancy.description.lower() for word in filter_words):
        #     filtered_vacancies.append(vacancy)

    return filtered_vacancies