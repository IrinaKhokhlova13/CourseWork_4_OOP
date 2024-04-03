from src.classes import HeadHunterAPI
from src.jsonwr import JsonWriteReader
from src.vacancy import Vacancy

def filter_vacancies(vacancy_objects, words):
    current_list = []
    if not words:
        return vacancy_objects

    for vacancy in vacancy_objects:
        if any(word.lower() in vacancy.requirement.lower() for word in words):
            current_list.append(vacancy)
    return current_list


def user_choice_hh():
    vacancy_name = input('Напишите название интерисующей вас профессии: \n')
    hh_api = HeadHunterAPI()
    from_hh = hh_api.get_vacancies(vacancy_name)
    vacancy_objects = Vacancy.from_dict(from_hh)
    print('Список вакансий с сайта "HeadHunter": \n')
    key_words = input('По каким ключевым словам найти вакансии?').split()
    filtered_vacancy = filter_vacancies(vacancy_objects, key_words)
    sortered_vacancy = sorted(filtered_vacancy, reverse=True)
    top_vacancy = input('Сколько вакансий вывести?')
    top_vacancies = sortered_vacancy[:int(top_vacancy)]
    for number, vacancy in enumerate(top_vacancies, 1):
        print(f'{number}. {vacancy}')
    print('Записать, отсортированные по зарплате данные в JSON файл? Ответьте в формате "Да", "Нет"\n')
    user_answer = input('Да\Нет \n').lower()
    if user_answer not in ['да']:
         print('Спасибо за использование программы')
    else:
        jsonfile = JsonWriteReader()
        jsonfile.add_vacancy(top_vacancies)



def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """
    print('Добро пожаловать! С помощью данной программы вы можете найти подходящую вакансию на сайте HeadHunter. \n'
          'Чтобы продолжить введите "Начать".\n'
          'Чтобы выйти из программы введите "Выход".\n')

    while True:
        user_choice_platform = input().lower()
        if user_choice_platform == 'начать':
            print('HeadHunter')
            user_choice_hh()
            break
        elif user_choice_platform == 'выход':
            print('До встречи')
            break
        else:
            print('Неверный запрос')
            break


if __name__ == '__main__':
    user_interaction()