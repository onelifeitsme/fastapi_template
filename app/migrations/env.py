from logging.config import fileConfig
from pathlib import Path
from sqlalchemy import engine_from_config
from sqlalchemy import pool
import sys
sys.path.append(str(Path(__file__).parent.parent))
from app.config import settings
from alembic import context
from app.database import Base
target_metadata = Base.metadata


config = context.config
section = config.config_ini_section
config.set_section_option(section, "DB_HOST", settings.DB_HOST)
config.set_section_option(section, "DB_PORT", str(settings.DB_PORT))
config.set_section_option(section, "DB_USER", settings.DB_USER)
config.set_section_option(section, "DB_NAME", settings.DB_NAME)
config.set_section_option(section, "DB_PASS", settings.DB_PASS)


if config.config_file_name is not None:
    fileConfig(config.config_file_name)


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
