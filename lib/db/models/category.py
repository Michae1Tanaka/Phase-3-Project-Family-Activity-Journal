from lib.helpers.database_utils import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.db.models.activity_category_association import activity_category


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    _category_name = Column("category_name", String, unique=True)

    activities = relationship(
        "Activity",
        secondary=activity_category,
        back_populates="categories",
    )

    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        if isinstance(category_name, str) and 0 < len(category_name) <= 32:
            self._category_name = category_name
        elif not isinstance(category_name, str):
            raise TypeError("Category name must be a string.")
        else:
            raise ValueError(
                "Category name must be in between the characters of 0 and 33."
            )

    def delete_category(self, session):
        session.delete(self)

    @classmethod
    def add_category(cls, category_name):
        new_category = Category(category_name=category_name)
        return new_category

    def __repr__(self):
        return f"<Category {self.category_name}>"
