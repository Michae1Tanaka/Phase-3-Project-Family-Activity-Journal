from database_utils import Base, engine


def create_tables():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_tables()
