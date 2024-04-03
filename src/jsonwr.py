import json
from pathlib import Path
from config import ROOT_DIR


class JsonWriteReader:
    """
    Запись и чтение json файл
    """

    def __init__(self):
        self.file_path = Path(ROOT_DIR, 'vacancies.json')
        if not self.file_path.is_file():
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump([], file)

    def add_vacancy(self, vacancy_list):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            vacancies = json.load(file)
            for vacancy in vacancy_list:
                current_dict = {
                    'vacancy_title': vacancy.vacancy_title,
                    'town': vacancy.town,
                    'salary_from': vacancy.salary_from,
                    'salary_to': vacancy.salary_to,
                    'requirement': vacancy.requirement,
                    'url': vacancy.url
                }
                vacancies.append(current_dict)
            with open(self.file_path, 'w', encoding='utf-8') as file_1:
                json.dump(vacancies, file_1)
