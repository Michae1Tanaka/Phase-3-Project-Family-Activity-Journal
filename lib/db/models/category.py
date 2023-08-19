from lib.helpers.database_utils import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.db.models.activity_category_association import activity_category


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    _category_name = Column("category_name", String, unique=True)

    activities = relationship(
        "Activity", secondary=activity_category, back_populates="categories"
    )

    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        if isinstance(category_name, str) and 0 < len(category_name) < 64:
            self._category_name = category_name

    def __repr__(self):
        return f"<Category {self.category_name}>"
