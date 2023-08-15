from sqlalchemy import Table, Integer, ForeignKey, MetaData, Column

metadata = MetaData()


activity_category_association = Table(
    "activity_category_association",
    metadata,
    Column("activity_id", Integer, ForeignKey("activities.id")),
    Column("category_id", Integer, ForeignKey("categories.id")),
)
