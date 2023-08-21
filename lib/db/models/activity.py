from ...helpers.database_utils import Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from lib.db.models.activity_category_association import activity_category
from datetime import date


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True)
    _name = Column("name", String)
    _description = Column("description", String)
    _notes = Column("notes", String)
    _location = Column("location", String)
    _weather = Column("weather", String)
    _date = Column("date", Date)

    photos = relationship("Photo", back_populates="activity")
    categories = relationship(
        "Category", secondary=activity_category, back_populates="activities"
    )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 0 < len(name) <= 68:
            self._name = name
        else:
            raise Exception(
                "The activity name must be a string and between 0 and 69 characters."
            )

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, activity_description):
        if (
            isinstance(activity_description, str)
            and 0 < len(activity_description) <= 68
        ):
            self._description = activity_description
        else:
            raise Exception(
                "A description must be a string and in between 0 and 69 characters."
            )

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, new_note):
        if isinstance(new_note, str) and 0 < len(new_note) <= 68:
            self._notes = new_note
        else:
            raise Exception(
                "A note must be a string and in between 0 and 69 characters."
            )

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        if (
            isinstance(location, str)
            and 0 < len(location) <= 68
            and 0 < location.count(",") <= 2
        ):
            self._location = location
        else:
            raise Exception(
                "The location must be written as a string, between 0 and 69 characters, and follow the formats such as 'City, Region, Country' or just 'City, Country'."
            )

    @property
    def weather(self):
        return self._weather

    @weather.setter
    def weather(self, weather):
        weather_conditions = (
            "Clear",
            "Cloudy",
            "Rainy",
            "Snowy",
            "Windy",
            "Foggy",
            "Hot",
            "Cold",
            "Mild",
            "Sunny",
        )
        if weather in weather_conditions:
            self._weather = weather
        else:
            raise Exception(
                "Weather must be 'Clear', 'Cloudy', 'Rainy', 'Snowy', 'Windy', 'Foggy', 'Hot', 'Cold', 'Mild', or 'Sunny' "
            )

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date_str):
        if self._is_valid_date(date_str):
            self._date = date.fromisoformat(date_str)
        else:
            raise Exception("Invalid date format. It must be 'YYYY-MM-DD")

    @staticmethod
    def _is_valid_date(date_str):
        try:
            date.fromisoformat(date_str)
            return True
        except ValueError:
            return False

    @classmethod
    def add_activity(cls, name, description, notes, location, date, weather):
        new_activity = Activity(
            name=name,
            description=description,
            notes=notes,
            location=location,
            date=date,
            weather=weather,
        )
        return new_activity

    def update_activity(
        self,
        name=None,
        description=None,
        notes=None,
        location=None,
        date=None,
        weather=None,
    ):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if notes is not None:
            self.notes = notes
        if location is not None:
            self.location = location
        if date is not None:
            self.date = date
        if weather is not None:
            self.weather = weather

    @classmethod
    def get_all_activities(cls, session):
        all_activities = session.query(cls).all()
        return all_activities

    def __repr__(self):
        formatted_date = f"{self._date.month}-{self._date.day}-{self._date.year}"

        return (
            f"<Activity name: {self.name}> \n\n"
            + f"<Description: {self.description}> \n\n"
            + f"<Notes: {self.notes}> \n\n"
            + f"<Location: {self.location}> \n\n"
            + f"<Weather: {self.weather}> \n\n"
            + f"<Date: {formatted_date}>"
        )
