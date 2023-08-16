from ...helpers.database_utils import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.db.models.activity_category_association import activity_category


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    notes = Column(String)
    location = Column(String)
    weather = Column(String)

    photos = relationship("Photo", back_populates="activity")
    categories = relationship(
        "Category", secondary=activity_category, back_populates="activities"
    )

    def __repr__(self):
        return (
            f"<Activity {self.name}> \n"
            + f"<Description: {self.description}> \n"
            + f"<Notes: {self.notes}> \n"
            + f"<Location: {self.location}> \n"
            + f"<Weather: {self.weather}> \n"
        )
