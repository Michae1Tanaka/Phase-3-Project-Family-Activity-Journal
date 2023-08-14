from helper import Base
from sqlalchemy import Column, Integer, String


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True)
    name = Column(String())
    description = Column(String()())
    notes = Column(String())
    location = Column(String())
    weather = Column(String())
