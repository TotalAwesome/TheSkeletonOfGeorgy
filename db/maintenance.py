"""

    Модель и логика по техработам

"""

from .base import *


class Maintenance(BaseModel):

    __tablename__ = 'maintenance'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    begin_at = Column(DateTime, comment="Начало работ")
    end_at = Column(DateTime, comment="Окончание работ")
    raw_date = Column(String, comment="Сырая строка с началом и окончанием (На всякий случай)")
    is_notified = Column(Boolean, comment="Отправлено ли уведомление")
