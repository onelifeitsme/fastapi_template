# from database import Base
from sqlalchemy import Column, Integer, String, MetaData, Table, JSON


metadata = MetaData()


roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, unique=True, nullable=False),
    Column("permissions", JSON),
)