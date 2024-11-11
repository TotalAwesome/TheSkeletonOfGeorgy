"""

    Модели и логика капчи
    Question = Вопрос с вариантами ответов
    AnswerOption = Вариант ответа
    Subject = Испытуемый

"""

from .base import *

class Question(BaseModel):

    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False, comment="Текст вопроса")
    answer_options = relationship('AnswerOption', backref='questions')


class AnswerOption(BaseModel):

    __tablename__ = 'answer_options'

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    text = Column(String, nullable=False, comment="Текст ответа")
    is_valid = Column(Boolean, default=False, comment="Верный ответ?")
