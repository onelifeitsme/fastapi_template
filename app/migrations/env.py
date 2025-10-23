from logging.config import fileConfig
from pathlib import Path
import sys

from sqlalchemy import engine_from_config, pool
from alembic import context

# Добавляем корень проекта в sys.path, чтобы Python видел app и config
sys.path.append(str(Path(__file__).parent.parent))

from app.config import settings
from app.database import Base

# Импортируем **все модули с моделями**, чтобы они зарегистрировались в Base.metadata
from app.models import product  # НЕ from app.models.product import Product

# target_metadata должен идти после импорта всех моделей
target_metadata = Base.metadata

# Настройка конфигурации Alembic
config = context.config
section = config.config_ini_section

# Подставляем реальные значения из settings
config.set_section_option(section, "DB_HOST", settings.DB_HOST)
config.set_section_option(section, "DB_PORT", str(settings.DB_PORT))
config.set_section_option(section, "DB_USER", settings.DB_USER)
config.set_section_option(section, "DB_NAME", settings.DB_NAME)
config.set_section_option(section, "DB_PASS", settings.DB_PASS)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
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
    """Run migrations in 'online' mode."""
    # Для Alembic используем синхронный движок, даже если приложение асинхронное
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
