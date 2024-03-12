class Vacancy:
    """
    Информация о вакансии
    """
    def __init__(self, vacancy_title, city, salary_from, salary_to, type_of_employment, url):
        self.vacancy_title: str = vacancy_title
        self.city: str = city
        self.salary_from: int = salary_from
        self.salary_to: int = salary_to
        self.type_of_employment: str = type_of_employment
        self.url: str = url

    def __str__(self):
        return f'название вакансии: {self.vacancy_title}\n' \
               f'город: {self.city}\n' \
               f'зарплата от: {self.salary_from}\n' \
               f'зарплата до: {self.salary_to}\n' \
               f'тип занятости: {self.type_of_employment}\n' \
               f'ссылка: {self.url}\n'

    def to_dict(self):
        """
        Возвращает вакансию в виде словаря
        """
        return {
            'vacancy_title': self.vacancy_title,
            'town': self.city,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'employment': self.type_of_employment,
            'url': self.url
        }

    @staticmethod
    def from_dict(vacancy_dict):
        """
        Возвращает вакансию в виде списка
        """
        return Vacancy(
            vacancy_dict['vacancy_title'],
            vacancy_dict['town'],
            vacancy_dict['salary_from'],
            vacancy_dict['salary_to'],
            vacancy_dict['employment'],
            vacancy_dict['url']
        )

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError('Вакансию можно сравнивать только с вакансией')
        return self.salary_from < other.salary_from


class Vacancies:
    """ Обработка списка всех вакансий"""

    def __init__(self):
        self.__all_vacancies = []

    def add_vacancies(self, new_vacancies):
        self.__all_vacancies += new_vacancies

    def delete_vacancies(self, old_vacancies):
        for i in old_vacancies:
            self.__all_vacancies.remove(i)

    def sort_vacancies_by_salary(self):
        self.__all_vacancies.sort(reverse=True)

    @property
    def all_vacancies(self):
        return self.__all_vacancies

    def to_list_dict(self):
        dict_vacancies = []
        for i in self.__all_vacancies:
            dict_vacancies.append(i.to_dict())
        return dict_vacancies