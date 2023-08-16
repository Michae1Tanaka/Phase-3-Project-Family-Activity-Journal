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


def delete_records():
    session.query(Photo).delete()
    session.query(Activity).delete()
    session.query(Category).delete()


def create_photos():
    photos = []
    for _ in range(60):
        photo = Photo(
            photo_description=fake.paragraph(nb_sentences=1),
            url=fake.image_url(),
            activity=rc(activities),
        )
        photos.append(photo)
    session.add_all(photos)
    session.commit()
    return photos


def create_activities():
    weather_options = ["cloudy", "sunny", "rainy", "snowy"]
    activities = []

    for _ in range(30):
        activity = Activity(
            name=fake.paragraph(nb_sentences=1),
            description=fake.paragraph(nb_sentences=1),
            notes=fake.paragraph(nb_sentences=1),
            location=fake.city() + ", " + fake.state(),
            weather=rc(weather_options),
        )
        activities.append(activity)
    session.add_all(activities)
    session.commit()
    return activities


def create_categories():
    category_names = ["Beach", "Outdoors", "Educational", "Park", "Theme Park"]
    categories = [Category(category_name=name) for name in category_names]

    session.add_all(categories)
    session.commit()
    return categories


if __name__ == "__main__":
    delete_records()
    activities = create_activities()
    photos = create_photos()
    category = create_categories()

    session.close()
