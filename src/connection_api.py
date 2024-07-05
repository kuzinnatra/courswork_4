import requests
from abc import ABC, abstractmethod

class AbstractApi(ABC):
    @abstractmethod
    def get_response(self, url):
        pass

    @abstractmethod
    def get_vacancies(self, text, per_page):
        pass

    @abstractmethod
    def get_filter_vacancies(self, text, per_page):
        pass


class HH(AbstractApi):
    """
    Класс для работы с API HeadHunter
    """
    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"

    def get_response(self):
        response = requests.get(self.__url)
        return response



    def get_vacancies(self, per_page: int, text: str = ''):
        self.per_page = per_page
        self.text = text
        params = {'text': self.text, 'page': 0, 'per_page': self.per_page}
        response = requests.get(self.__url, params)
        return response.json()['items']


    def get_filter_vacancies(self, per_page: int, text: str = ''):
        filtered_vacancies = []
        vacancies = self.get_vacancies(per_page, text)
        for vacancy in vacancies:
            filtered_vacancies.append({
                "name": vacancy["name"],
                "salary": vacancy["salary"],
                "url": vacancy["alternate_url"],
                "employer": vacancy["employer"]["name"]
            })
        return filtered_vacancies






