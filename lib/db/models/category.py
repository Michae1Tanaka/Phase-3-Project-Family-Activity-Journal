from lib.helpers.database_utils import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.db.models.activity_category_association import activity_category


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    category_name = Column(String)

    activities = relationship(
        "Activity", secondary=activity_category, back_populates="categories"
    )

    def __repr__(self):
        return f"<Category {self.category_name}>"
