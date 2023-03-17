class Vacancy:
    __slots__ = ('job_title', 'job_link', 'job_description', 'job_salary')

    def __init__(self, job_title, job_link, job_description, job_salary):
        self.job_title = job_title
        self.job_link = job_link
        self.job_description = job_description
        self.job_salary = job_salary


    def __str__(self):
        return f"Название вакансии - {self.job_title}\nОписание: {self.job_description}\nЗарплата: {self.job_salary}\nСсылка на вакансию{self.job_link}"



class CountMixin:

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        pass



class HHVacancy(Vacancy):  # add counter mixin
    """ HeadHunter Vacancy """


    def __str__(self):
        return f'HH: {self.job_title}, зарплата: {self.job_salary} руб/мес'



class SJVacancy(Vacancy):  # add counter mixin
    """ SuperJob Vacancy """

    def __str__(self):
        return f'SJ: {self.job_title}, зарплата: {self.job_salary} руб/мес'


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    pass


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    pass