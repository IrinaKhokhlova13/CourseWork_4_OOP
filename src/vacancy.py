class Vacancy:
    """
    Информация о вакансии
    """

    def __init__(self, vacancy_title, town, salary_from, salary_to, requirement, url):
        self.vacancy_title: str = vacancy_title
        self.town: str = town
        self.salary_from: int = salary_from
        self.salary_to: int = salary_to
        self.requirement: str = requirement
        self.validate_requirement()
        self.url: str = url

    def validate_requirement(self):
        if not self.requirement:
            self.requirement = 'Описание не указано'

    def __str__(self):
        return f'название вакансии: {self.vacancy_title}\n' \
               f'город: {self.town}\n' \
               f'зарплата от: {self.salary_from}\n' \
               f'зарплата до: {self.salary_to}\n' \
               f'требование: {self.requirement}\n' \
               f'ссылка: {self.url}\n'


    @classmethod
    def from_dict(cls, vacancy_list):
        """
        Возвращает вакансию в виде списка
        """
        current_list = []
        for vacancy_dict in vacancy_list:
            current_list.append(
                cls(
                    vacancy_dict['vacancy_title'],
                    vacancy_dict['town'],
                    vacancy_dict['salary_from'],
                    vacancy_dict['salary_to'],
                    vacancy_dict['requirement'],
                    vacancy_dict['url']
                ))
        return current_list

    def get_salary(self):
        if self.salary_from and self.salary_to:
            res_salary = round((self.salary_from + self.salary_to)/2)
        elif not self.salary_from:
            res_salary = self.salary_to
        else:
            res_salary = self.salary_from
        return res_salary

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError('Вакансию можно сравнивать только с вакансией')
        return self.get_salary() < other.get_salary()

