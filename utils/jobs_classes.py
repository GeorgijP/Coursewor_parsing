class Vacancy:
    """
    Делает данные читабильными
    """
    __slots__ = ('job_title', 'job_link', 'job_description', 'job_salary')

    def __init__(self, job_title, job_link, job_description, job_salary):
        self.job_title = job_title
        self.job_link = job_link
        self.job_description = job_description
        self.job_salary = job_salary


    def __str__(self):
        return f"Название вакансии - {self.job_title}\nОписание: {self.job_description}\nЗарплата: {self.job_salary}\nСсылка на вакансию{self.job_link}"
