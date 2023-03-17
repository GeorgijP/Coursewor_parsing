import requests
from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def get_request(self):
        ...

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        pass


class HH(Engine):
    def get_request(self):
        url = "https://api.hh.ru/vacancies/"
        par = {'text': 'python', 'area': 113}
        self.request = requests.get(url, params=par).json()
        return self.request["items"]


class Superjob(Engine):
    def get_request(self):
        url = 'https://api.superjob.ru/2.0/vacancies/'
        headers = {"X-Api-App-Id": "v3.r.137427491.f38a88a81cfa9ab6d514bb52ef8d8d9d17c470cb.30e3a8df42b0b4854ccd429931ac7d3a7b8e3c34"}
        self.request = requests.get(url, headers=headers).json()
        return self.request

hh = HH()
# print(hh.get_request())

sj = Superjob()
# print(sj.get_request())
