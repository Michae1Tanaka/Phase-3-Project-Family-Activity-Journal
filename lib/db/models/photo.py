from lib.helpers.database_utils import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer(), primary_key=True)
    _photo_description = Column("photo_description", String())
    _url = Column("url", String())

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

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, photo_url):
        if isinstance(photo_url, str) and self.is_valid_image(photo_url):
            self._url = photo_url
        else:
            raise Exception(
                "Photo url must end in either .jpeg, .png, .pdf, .jpg, or .heic and must be a string."
            )

    @classmethod
    def add_photo(cls, photo_description, url, activity_id):
        new_photo = Photo(
            photo_description=photo_description, url=url, activity_id=activity_id
        )
        return new_photo

    @staticmethod
    def is_valid_image(source):
        allowed_extensions = ["jpeg", "png", "pdf", "jpg", "heic"]
        extension = source.split(".")[-1]
        return extension.lower() in allowed_extensions

    def __repr__(self):
        return (
            f"<Photo {self.photo_description}>\n"
            + f"<URL: {self.url}>\n"
            + f"<Activity ID: {self.activity_id}>\n"
        )
