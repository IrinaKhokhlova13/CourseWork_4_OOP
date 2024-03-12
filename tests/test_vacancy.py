import pytest
from src.vacancy import Vacancy


@pytest.fixture
def vacancy():
    vacancy_ = Vacancy("Backend-разработчик, удаленно",
                "Москва",
                100000,
                140000,
                "Полная занятость",
                "https://hh.ru/vacancy/94112195")
    return vacancy_



def test__init__(vacancy):
    assert vacancy.vacancy_title == "Backend-разработчик, удаленно"
    assert vacancy.city == "Москва"
    assert vacancy.salary_from == 100000
    assert vacancy.salary_to == 140000
    assert vacancy.type_of_employment == "Полная занятость"
    assert vacancy.url == "https://hh.ru/vacancy/94112195"