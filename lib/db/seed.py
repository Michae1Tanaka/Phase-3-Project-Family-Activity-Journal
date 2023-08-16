from faker import Faker
import random
from random import choice as rc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models.activity import Activity
from .models.photo import Photo
from .models.category import Category
from .models.activity_category_association import activity_category_association

fake = Faker()
