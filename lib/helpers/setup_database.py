from lib.helpers.database_utils import Base, engine, Session
from lib.db.models.activity import Activity
from lib.db.models.activity_category_association import activity_category
from lib.db.models.category import Category
from lib.db.models.photo import Photo


def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session = Session()
    session.commit()


if __name__ == "__main__":
    create_tables()
