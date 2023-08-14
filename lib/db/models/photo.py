from helpers import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer(), primary_key=True)
    url = Column(String())

    activity_id = Column(Integer(), ForeignKey("activities.id"))
    activity = relationship("Activity", back_populates="photo")
