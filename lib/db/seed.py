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
