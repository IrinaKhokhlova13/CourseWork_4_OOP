import pytest
from src.vacancy import Vacancy
from abc import ABC
from src.abstract_classes import GetVacancies
from src.classes import HeadHunterAPI


@pytest.fixture
def vacancy():
    vacancy_ = Vacancy("Backend-разработчик, удаленно",
                "Москва",
                100000,
                140000,
                "Полная занятость",
                "https://hh.ru/vacancy/94112195")
    return vacancy_


def test_issubclass():
    assert issubclass(GetVacancies, ABC)
    assert issubclass(HeadHunterAPI, GetVacancies)