from sqlalchemy import Column, Integer, String
from database import Base

class Term(Base):
    __tablename__ = "terms"

    id = Column(Integer, primary_key=True, index=True)
    english = Column(String, nullable=False)
    russian = Column(String, nullable=True)
    turkmen = Column(String, nullable=True)
    abbreviation = Column(String, nullable=True)
    category = Column(String, nullable=True)
    description_en = Column(String, nullable=True)
    description_ru = Column(String, nullable=True)
    description_tm = Column(String, nullable=True)
