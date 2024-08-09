from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase
from config import settings


engine = create_engine(
    settings.DATABASE_URL_psycopg,
    echo=True,
)

