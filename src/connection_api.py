import requests
from abc import ABC, abstractmethod

class AbstractApi(ABC):
    @abstractmethod
    def get_response(self, url):
        pass
    @abstractmethod
    def get_vacancies(self, per_page, text):
        pass


class HH(AbstractApi):
    """
    Класс для работы с API HeadHunter
    """
    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"

    def get_url(self):
        return self.__url

    def get_response(self):
        response = requests.get(self.__url)
        return response

    def get_vacancies(self, per_page: int, text: str = ''):
        self.per_page = per_page
        self.text = text
        params = {'text': self.text, 'page': 0, 'per_page': self.per_page}
        response = requests.get(self.__url, params)
        return response.json()['items']
