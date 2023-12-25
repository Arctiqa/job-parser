from src.api_class import HeadHunterAPI, SuperJobAPI
from src.jsonsaver import JSONSaver
from utils import requirements_filter, get_top_n_vacancies, vacancies_info, sort_vacancies
from dotenv import load_dotenv

load_dotenv()


def main():
    while True:
        print("Выберите платформу (HeadHunter/SuperJob): ")

        platform = input().lower()

        if platform not in ["headhunter", "superjob"]:
            continue

        print("Введите название вакансии: ")
        user_vacancy = input()

        print("Введите количество вакансий для отображения: ")
        top_n = int(input())

        print("Введите ключевые слова для фильтрации вакансий (через пробел): ")
        filter_words = input().split()

        hh_api = HeadHunterAPI()
        sj_api = SuperJobAPI()

        if platform == "headhunter":
            platform_vacancies = hh_api.get_vacancies(user_vacancy)
        else:
            platform_vacancies = sj_api.get_vacancies(user_vacancy)

        filtered_vacancies = requirements_filter(platform_vacancies, filter_words)

        if not filtered_vacancies:
            print("Нет вакансий, соответствующих заданным критериям.")
            continue

        # Сортировка вакансий
        sorted_vacancies = sort_vacancies(filtered_vacancies)
        top_vacancies = get_top_n_vacancies(sorted_vacancies, top_n)

        print("Результаты поиска:")
        vacancies_info(top_vacancies)

        save_choice = input("Хотите сохранить найденные вакансии? (да/нет): ").lower()
        if save_choice == "да":
            json_saver = JSONSaver("vacancies.json")
            for vacancy in top_vacancies:
                json_saver.add_vacancy(vacancy)
            json_saver.save_to_file()


if __name__ == "__main__":
    main()
