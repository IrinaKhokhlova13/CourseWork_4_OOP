from abc import ABC, abstractmethod


class GetVacancies(ABC):
    """
    Абстрактный класс для метода получения вакансий
    """
    @abstractmethod
    def get_vacancies(self, name_job):
        pass


class JsonWR(ABC):
    """
    Запись полученных вакансий в файл json и чтение
    """
    @abstractmethod
    def file_reader_writer(self):
        pass