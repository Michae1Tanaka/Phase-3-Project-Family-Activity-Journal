from .helpers.database_utils import Session
from .db.models.activity import Activity
from .db.models.photo import Photo
from .db.models.category import Category
from .db.models.activity_category_association import activity_category
import ipdb

if __name__ == "__main__":
    session = Session()
    ipdb.set_trace()
