from src.vacancy_ import Vacancy


def sort_vacancies(vacancies):
    """
    Сортирует вакансии по зарплате.
    :param vacancies: Список вакансий
    :return: Отсортированный список
    """
    return sorted(vacancies, key=lambda x: x.salary, reverse=True)


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


def requirements_filter(vacancies, searching_words):
    """
    Фильтрует вакансии по ключевым словам.
    :param vacancies: Список вакансий
    :param searching_words: Список ключевых слов для фильтрации
    :return: Отфильтрованный список
    """
    filtered_vacancies = []
    for vacancy in vacancies:
        if 'vacancyRichText' in vacancy and vacancy['vacancyRichText'] is not None:
            if all(word in vacancy['vacancyRichText'] for word in searching_words):
                title = vacancy['profession']
                link = vacancy['link']
                if vacancy['payment_from'] == 0:
                    salary = vacancy['payment_to']
                else:
                    salary = vacancy['payment_from']
                description = vacancy['vacancyRichText']
                vac = Vacancy(title, link, salary, description)
                filtered_vacancies.append(vac)
        elif 'snippet' in vacancy:
            if all(word in vacancy['snippet']['requirement'] for word in searching_words):
                title = vacancy['name']
                link = vacancy['alternate_url']
                if 'salary' in vacancy and vacancy['salary'] is not None and 'from' in vacancy['salary'] and \
                        vacancy['salary']['from'] is not None:
                    salary = vacancy['salary']['from']
                elif 'salary' in vacancy and vacancy['salary'] is not None and 'to' in vacancy['salary'] and \
                        vacancy['salary']['to'] is not None:
                    salary = vacancy['salary']['to']
                else:
                    salary = 0
                print(salary)
                description = vacancy['snippet']['requirement']
                vac = Vacancy(title, link, salary, description)
                filtered_vacancies.append(vac)

    return filtered_vacancies
