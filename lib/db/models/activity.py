from ...helpers.database_utils import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.db.models.activity_category_association import activity_category
from datetime import date


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True)
    _name = Column(String)
    _description = Column(String)
    _notes = Column(String)
    location = Column(String)
    weather = Column(String)
    date = Column(String)

    photos = relationship("Photo", back_populates="activity")
    categories = relationship(
        "Category", secondary=activity_category, back_populates="activities"
    )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 0 < len(name) < 64:
            self._name = name
        else:
            raise Exception("Name must be a string.")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, activity_description):
        if isinstance(activity_description, str) and 0 < len(activity_description) < 64:
            self._description = activity_description
        else:
            raise Exception("Description must be a string")

    @classmethod
    def add_activity(cls, session, name, description, notes, location, date, weather):
        new_activity = Activity(
            name=name,
            description=description,
            notes=notes,
            location=location,
            date=date,
            weather=weather,
        )
        session.add(new_activity)
        session.commit()

    def __repr__(self):
        date_split = self.date.split("-")
        formatted_date = f"{date_split[1]}-{date_split[2]}-{date_split[0]}"
        return (
            f"<Activity {self.name}> \n"
            + f"<Description: {self.description}> \n"
            + f"<Notes: {self.notes}> \n"
            + f"<Location: {self.location}> \n"
            + f"<Weather: {self.weather}> \n"
            + f"<Date: {formatted_date}>"
        )
