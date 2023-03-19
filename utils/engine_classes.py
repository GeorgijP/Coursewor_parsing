import json

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
        items = []

        for i in range(1):
            url = "https://api.hh.ru/vacancies"
            par = {
                'text': 'python',
                'areas': 113,
                'page': i
            }
            self.request = requests.get(url, params=par).json()
            if self.request == []:
                continue
            for y in range(20):
                items.append(self.request['items'][y]['name'])
                items.append(self.request['items'][y]['alternate_url'])
                items.append(self.request['items'][y]['snippet']['requirement'])
                items.append(self.request['items'][y]['salary'])

        with open('vacanciesHH.json', 'w') as f:
            json.dump(items, f, indent=4)


class Superjob(Engine):
    def get_request(self):
        items = []

        for i in range(1):
            url = 'https://api.superjob.ru/2.0/vacancies/'
            headers = {
                "X-Api-App-Id": "v3.r.137427491.f38a88a81cfa9ab6d514bb52ef8d8d9d17c470cb.30e3a8df42b0b4854ccd429931ac7d3a7b8e3c34"
            }
            par = {
                'keywords': 'python',
                'page': i,
                'count': 100
            }
            self.request = requests.get(url, headers=headers, params=par).json()
            if self.request == []:
                continue
            for y in range(100):
                items.append(self.request['objects'][y]['profession'])
                items.append(self.request['objects'][y]['link'])
                items.append(self.request['objects'][y]['candidat'])
                items.append(self.request['objects'][y]['payment_from'])

        with open('vacanciesSJ.json', 'w') as f:
            json.dump(items, f, indent=4)

