import requests
import json
from src.abstract_classes import GetVacancies
from src.vacancy import Vacancy
from src.jsonwr import JsonWriteReader

def user_choice_hh():
    vacancy_name = input('Напишите название интерисующей вас профессии: \n')
    hh_api = HeadHunterAPI()
    print('Сколько вывести страниц? \n')
    pages = int(input())
    from_hh = hh_api.get_vacancies(vacancy_name, pages)
    print('Список вакансий с сайта "HeadHunter": \n')
    for i in from_hh:
        print(i)
    print('Записать, отсортированные по зарплате данные в JSON файл? Ответьте в формате "Да", "Нет"\n')
    user_answer = input('Да\Нет \n').lower()
    if user_answer not in ['да']:
        print('Спасибо за использование программы')
    else:
        jsonfile = JsonWriteReader()
        jsonfile.add_vacancies(from_hh)
        jsonfile.sort_vacancies_by_salary()
        jsonfile.file_writer()
        return jsonfile


class HeadHunterAPI(GetVacancies):
    """ Класс для подключения к сайту hh.ru"""
    def get_vacancies(self, name_job, pages):
        hh_list = []
        for i in range(pages):
            params = {
                'text': name_job,
                'per_page': 99,
                'pege': i
            }
            response = requests.get('https://api.hh.ru/vacancies', params=params)
            response_json = response.json()
            for i in response_json['items']:
                hh_title = i['name']
                if not (i['area']) is None:
                    hh_city = i['area']['name']
                else:
                    hh_city = None
                if not ((i['salary'] is None) or i['salary']['from'] is None):
                    salary_from = i['salary']['from']
                    salary_to = i['salary']['to']
                else:
                    salary_from = 0
                    salary_to = 0
                employment_name = i['employment']['name']
                hh_url = i['alternate_url']
                hh_vacancy = Vacancy(hh_title, hh_city, salary_from, salary_to, employment_name, hh_url)
                hh_list.append(hh_vacancy)
        return hh_list




