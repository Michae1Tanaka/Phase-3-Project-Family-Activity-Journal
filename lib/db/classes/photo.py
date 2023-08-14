from helpers import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer(), primary_key=True)
    url = Column(String())
