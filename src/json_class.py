import json
from abc import ABC, abstractmethod
from src.vacancy import Vacancy

class AbstractJsonClass(ABC):
    @abstractmethod
    def write_data(self, vac):
        pass
    @abstractmethod
    def get_vacancies(self):
        pass
    @abstractmethod
    def delete_vacancy(self):
        pass


class GetJson(AbstractJsonClass):
    def __init__(self, filename="vacancies.json"):
        """указываем файл для сохранения данных """
        self.filename = f"data/{filename}"
    def write_data(self, vac):
        """записываем данные в файл"""
        with open(self.filename, 'w') as f:
            json.dump(vac, f, ensure_ascii=False, indent=4)

    def get_vacancies(self):
        """отображаем вакансии по выбранным критериям"""
        with open(self.filename, 'r') as f:
            data = json.load(f)
        vacancies = []
        for vacancy in data:
            vacancies.append(Vacancy(
                name=vacancy['name'],
                salary=vacancy['salary'],
                url=vacancy['alternate_url'],
                employer=vacancy['employer']['name']
            ))

        return vacancies

    def delete_vacancy(self):
        """очистить файл с вакансиями"""
        with open(self.filename, 'w'):
            pass




