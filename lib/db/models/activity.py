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
    _location = Column(String)
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
        if isinstance(name, str) and 0 < len(name) <= 64:
            self._name = name
        else:
            raise Exception(
                "The activity name must be a string and in between 0 and 65 characters."
            )

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, activity_description):
        if (
            isinstance(activity_description, str)
            and 0 < len(activity_description) <= 65
        ):
            self._description = activity_description
        else:
            raise Exception(
                "A description must be a string and in between 0 and 65 characters."
            )

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, new_note):
        if isinstance(new_note, str) and 0 < len(new_note) <= 128:
            self._description = new_note
        else:
            raise Exception(
                "A note must be a string and in between 0 and 129 characters."
            )

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        if (
            isinstance(location, str)
            and 0 < len(location) <= 64
            and 0 < location.count(",") <= 2
        ):
            self._location = location
        else:
            raise Exception(
                "The location must be written as a string, between 1 and 64 characters, and typically follow formats such as 'City, Region, Country' or just 'City, Country'. Please adjust based on your specific location."
            )

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
