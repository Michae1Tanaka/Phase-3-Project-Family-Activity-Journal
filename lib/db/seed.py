from faker import Faker
from random import choice as rc
from ..helpers.database_utils import Session
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
    session.query(activity_category).delete()


def create_photos(activities):
    photos = []
    allowed_extensions = [".jpg", ".jpeg", ".png", ".gif", ".heic"]
    for _ in range(60):
        photo = Photo(
            _photo_description=fake.paragraph(nb_sentences=1),
            _url=fake.image_url() + rc(allowed_extensions),
            activity_id=rc(activities).id,
        )
        photos.append(photo)
    session.add_all(photos)
    session.commit()
    return photos


def create_activities():
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
    activities = []

    for _ in range(47):
        activity = Activity(
            _name=fake.paragraph(nb_sentences=1),
            _description=fake.paragraph(nb_sentences=1),
            _notes=fake.paragraph(nb_sentences=1),
            _location=fake.city() + ", " + fake.state(),
            _weather=rc(weather_conditions),
            date=fake.date(),
        )
        activities.append(activity)
    session.add_all(activities)
    session.commit()
    return activities


def create_categories():
    category_names = ["Beach", "Outdoors", "Educational", "Park", "Theme Park"]
    categories = [Category(_category_name=name) for name in category_names]

    session.add_all(categories)
    session.commit()
    return categories


def create_activity_category(activities, categories):
    for _ in range(len(activities)):
        activity = rc(activities)
        category = rc(categories)
        activity.categories.append(category)
        session.add(activity)
        session.commit()


if __name__ == "__main__":
    delete_records()
    activities = create_activities()
    photos = create_photos(activities)
    categories = create_categories()
    create_activity_category(activities, categories)
    session.close()
