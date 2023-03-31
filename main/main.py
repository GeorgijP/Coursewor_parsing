# Импортируем все классы.
from utils.connector import Connector
from utils.jobs_classes import Vacancy
from utils.engine_classes import HH, Superjob

# Запрашиваем у пользователя ключевое слово
keyword = str(input("Введите ключевое слово для поиска: ").lower())

# Создаем экземпляры классов в которых далее будут вызываться GET запросы. И передаем ключевое слово.
hh = HH(keyword)
sj = Superjob(keyword)

# Создаем экземпляр класса Connector и передаем в него результаты GET запросов путем вызова их методами get_request().
con = Connector(hh.get_request(), sj.get_request())
# Создаем JSON файлы
con.insert()
print('Файлы с вакансиями созданы')

# Пустой список для отсортированных вакансий
items = []
def jobs_class_activation():
    """
    Создает экземпляры класса Vacancy и помещает из в список items созданный ранее.
    """
    answer = str(input("Хотите вывести отсортированную информацию в консоль (yes/no): ").lower())
    if answer == 'yes':
        # Вызов метода класса Connector для сортировки.
        select = con.select()
        # Итерируем вакансии HH.ru и создаем экземпляры класса Vacancy
        for index_hh in range(len(select[0])):
            vac = Vacancy(select[0][index_hh][0], select[0][index_hh][1], select[0][index_hh][2], select[0][index_hh][3])
            # Проверка на пустой список
            if vac == []:
                continue
            else:
                items.append(vac)
        # Итерируем вакансии Superjob.ru и создаем экземпляры класса Vacancy
        for index_sj in range(len(select[1])):
            vac = Vacancy(select[1][index_sj][0], select[1][index_sj][1], select[1][index_sj][2], select[1][index_sj][3])
            # Проверка на пустой список
            if vac == []:
                continue
            else:
                items.append(vac)

    else:
        # Обижаемся на пользователя, потому что мы страрались
        print('А что так грубо? Ой всё.')


# Вызываем
jobs_class_activation()

# Выводим результат
for i in range(len(items)):
    print(f"{items[i]}\n")
