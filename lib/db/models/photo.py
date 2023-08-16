from lib.helpers.database_utils import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer(), primary_key=True)
    photo_description = Column(String())
    url = Column(String())

    activity_id = Column(Integer(), ForeignKey("activities.id"))
    activity = relationship("Activity", back_populates="photos")

    def __repr__(self):
        return (
            f"<Photo {self.photo_description}\n"
            + f"<URL: {self.url}\n"
            + f"<Activity ID: {self.activity_id}\n"
        )
