from faker import Faker
import random
from random import choice as rc
from ..helpers.database_utils import Session, engine
from .models.activity import Activity
from .models.photo import Photo
from .models.category import Category
from .models.activity_category_association import activity_category

fake = Faker()
session = Session()

weather_options = ["cloudy", "sunny", "rainy", "snowy"]


def delete_records():
    session.query(Photo).delete()
    session.query(Activity).delete()


def create_photos():
    photos = []
    for _ in range(10):
        photo = Photo(
            photo_description=fake.paragraph(nb_sentences=1),
            url=fake.image_url(),
            activity_id=rc(range(10)),
        )
        session.add(photo)
        session.commit()
        photos.append(photo)
    return photos


def create_activities():
    activities = []
    for _ in range(30):
        activity = Activity(
            name=fake.paragraph(nb_sentences=1),
            description=fake.paragraph(nb_sentences=1),
            notes=fake.paragraph(nb_sentences=1),
            location=fake.city() + ", " + fake.state(),
            weather=rc(weather_options),
        )
        session.add(activity)
        session.commit()
        activities.append(activity)
    return activities


if __name__ == "__main__":
    delete_records()
    photos = create_photos()
    activities = create_activities()
