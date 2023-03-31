import requests
import os
import jmespath
from abc import ABC, abstractmethod


class Engine(ABC):

    @abstractmethod
    def get_request(self):
        ...


class HH(Engine):
    """
    Делает GET запрос к api hh.ru
    """
    def __init__(self, keyword):
        self.keyword = keyword

    def get_request(self):
        items = []

        for i in range(10):
            url = "https://api.hh.ru/vacancies"
            par = {
                'text': self.keyword,
                'areas': 113,
                'page': i,
                'per_page': 100,
            }
            self.response = requests.get(url, params=par).json()
            if self.response == []:
                continue
            items.append(jmespath.search('items[*]', self.response)) # Такая конструкция быстрее обрабатывает данные

        return items


class Superjob(Engine):
    """
    Делает GET запрос к api Superjob.ru
    """
    def __init__(self, keyword):
        self.keyword = keyword
        self.api_key = os.environ.get('SECRET_KEY_SJ')

    def get_request(self):
        items = []

        for i in range(10):
            url = 'https://api.superjob.ru/2.0/vacancies/'
            headers = {
                "X-Api-App-Id": self.api_key
            }
            par = {
                'keywords': self.keyword,
                'page': i,
                'count': 100
            }
            self.response = requests.get(url, headers=headers, params=par).json()
            if self.response == []:
                continue
            items.append(jmespath.search('objects[*]', self.response)) # Такая конструкция быстрее обрабатывает данные

        return items
