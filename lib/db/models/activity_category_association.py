from sqlalchemy import Table, Integer, ForeignKey, MetaData, Column
from lib.helpers.database_utils import Base

metadata = MetaData()


activity_category = Table(
    "activity_category",
    Base.metadata,
    Column("activity_id", Integer, ForeignKey("activities.id")),
    Column("category_id", Integer, ForeignKey("categories.id")),
)
