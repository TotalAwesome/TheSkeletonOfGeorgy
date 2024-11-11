from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .captcha import AnswerOption, Question
from .maintenance import Maintenance
from .vacancies import Vacancy
from .base import BaseModel

engine = create_engine("sqlite:///georgy.db", echo=True)
Session = sessionmaker(autoflush=True, bind=engine)

BaseModel.metadata.create_all(bind=engine)

with Session(autoflush=False, bind=engine) as db:
    ans = AnswerOption()