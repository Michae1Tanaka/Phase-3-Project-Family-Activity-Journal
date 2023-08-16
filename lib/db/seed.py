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


def create_photos():
    photos = []
    for i in range(10):
        photo = Photo(
            photo_description=fake.paragraph(nb_sentences=1),
            url=fake.image_url(),
            activity_id=rc(range(10)),
        )
        session.add(photo)
        session.commit()
        photos.append(photo)
    return photos


if __name__ == "__main__":
    delete_records()
    photos = create_photos()
