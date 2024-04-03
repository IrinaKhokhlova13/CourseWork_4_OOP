import requests
import json
from src.abstract_classes import GetVacancies

class HeadHunterAPI(GetVacancies):
    """ Класс для подключения к сайту hh.ru"""

    def __init__(self):
        self.hh_vacancies = []

    def get_vacancies(self, name_job):
        # hh_list = []
        for i in range(20):
            params = {
                'text': name_job,
                'per_page': 99,
                'page': i,
                'search_field': 'name'
            }
            response = requests.get('https://api.hh.ru/vacancies', params=params)
            response_json = response.json()
            for i in response_json['items']:  # изменить на vacancy
                hh_title = i['name']
                hh_city = i['area']['name']
                salary_from = 0
                salary_to = 0
                if i['salary']:
                    if i['salary']['from']:
                        salary_from = i['salary']['from']
                    if i['salary']['to']:
                        salary_to = i['salary']['to']
                requirement = i["snippet"]["requirement"]
                hh_url = i['alternate_url']
                hh_vacancy = {'vacancy_title': hh_title, 'town': hh_city, 'salary_from': salary_from, 'salary_to': salary_to,
                              'requirement': requirement, 'url': hh_url}
                self.hh_vacancies.append(hh_vacancy)
        return self.hh_vacancies

