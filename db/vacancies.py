"""

    Модель и логика по вакансиям

"""

from .base import *

class Vacancy(BaseModel):

    __tablename__ = 'vacancies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    vacancy_id = Column(Integer, comment="Id вакансии с источника, например hh.ru")
    title = Column(String, comment="Название вакансии")
    salary_from = Column(Integer, comment="Доход от")
    salary_to = Column(Integer, comment="Доход до")
    work_schedule = Column(String, comment="Режим работы")
    employer_name = Column(String, comment="Наименование работодателя")
    published_at = Column(DateTime, comment="Дата публкиации вакансии (или обновления)")
    url = Column(String, comment="Ссылка на вакансию")
    is_notified = Column(Boolean, comment="Отправлено ли уведомление")
    currency = Column(String(10), default='RUR', comment="Валюта")
