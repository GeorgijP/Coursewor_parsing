import json

class Connector:
    """
    Создает экземпляры классов HH и Superjob.
    Записывает полученные данные в соответствующие файлы.
    Сортирует данные.
    """

    def __init__(self, data_HH, data_SJ):
        self.data_HH = data_HH
        self.data_SJ = data_SJ

    def insert(self):
        """
        Запись данных в файлы с сохранением структуры и исходных данных
        """
        with open('Vacancy_HH.json', 'w') as f:
            json.dump(self.data_HH, f, indent=4)

        with open('Vacancy_SJ.json', 'w') as f:
            json.dump(self.data_SJ, f, indent=4)

    def select(self):
        """
        Выборка нужной информации из фпйлов json
        Возвразщает 2 списка
        """
        items_HH = []
        items_SJ = []

        # Открываем файл и записываем его в переменную
        with open('Vacancy_HH.json', 'r') as file_HH:
            data_HH = json.load(file_HH)

            # Так как у на было произведено 10 запросов по 100 вакансий в каждом,
            # то пришлось вложить в цикл for еще один for
            # index_one принимает значения от 0 до 9,
            # а index_two от 0 до 99.
            # Таким образом мы вытягиваем 1000 вакансий
            for index_one in range(len(data_HH)):
                for index_two in range(len(data_HH[index_one])):
                    item = []
                    item.append(data_HH[index_one][index_two]['name'])
                    item.append(data_HH[index_one][index_two]['alternate_url'])
                    item.append(data_HH[index_one][index_two]['snippet']['requirement'])
                    if data_HH[index_one][index_two]['salary'] is None: # Проверка наличия зп в данных
                        item.append('Работадатель не указал зарплату')
                    else:
                        item.append(data_HH[index_one][index_two]['salary']['from'])
                    items_HH.append(item)

        # Тут все тоже самое, что и для файла Vacancy_HH.json, только для Vacancy_SJ.json
        with open('Vacancy_SJ.json', 'r') as file_SJ:
            data_SJ = json.load(file_SJ)
            for index_one in range(len(data_SJ)):
                for index_two in range(len(data_SJ[index_one])):
                    item = []
                    item.append(data_SJ[index_one][index_two]['profession'])
                    item.append(data_SJ[index_one][index_two]['link'])
                    item.append(data_SJ[index_one][index_two]['candidat'])
                    if data_SJ[index_one][index_two]['payment_from'] is None:
                        item.append('Работадатель не указал зарплату')
                    else:
                        item.append(data_SJ[index_one][index_two]['payment_from'])
                    items_SJ.append(item)

        return items_HH, items_SJ
