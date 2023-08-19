from lib.helpers.database_utils import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer(), primary_key=True)
    _photo_description = Column("photo_description", String())
    url = Column(String())

    activity_id = Column(Integer(), ForeignKey("activities.id"))
    activity = relationship("Activity", back_populates="photos")

    @property
    def photo_description(self):
        return self._photo_description

    @photo_description.setter
    def photo_description(self, photo_description):
        if isinstance(photo_description, str) and 0 < len(photo_description) <= 128:
            self._photo_description = photo_description
        else:
            raise Exception(
                "The photo description must be a string and in between 0 and 129 characters."
            )

    def __repr__(self):
        return (
            f"<Photo {self.photo_description}>\n"
            + f"<URL: {self.url}>\n"
            + f"<Activity ID: {self.activity_id}>\n"
        )
