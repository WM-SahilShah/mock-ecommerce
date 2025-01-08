from venv import logger
from alembic import context
from app.config.logging import logger
from app.config.settings import DB_URL
from app.database.database import Base
from app.database.models import User, Category, Cart, CartItem, Product # Unused imports imp for db
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig

# Access Alembic configuration
config = context.config
config.set_main_option("sqlalchemy.url", DB_URL)
if config.config_file_name:
    fileConfig(config.config_file_name)

def run_migrations_offline() -> None:
    """Run migrations in `offline` mode."""
    logger.info("Starting migrations in offline mode.")
    url = config.get_main_option("sqlalchemy.url")
    
    context.configure(
        url=url,
        target_metadata=Base.metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    try:
        with context.begin_transaction():
            logger.info("Running migrations...")
            context.run_migrations()
        logger.info("Migrations completed successfully in offline mode.")
    except Exception as e:
        logger.exception(f"An error occurred during offline migrations.")
        raise RuntimeError("Failed to run migrations in offline mode.") from e

def run_migrations_online() -> None:
    """Run migrations in `online` mode."""
    logger.info("Starting migrations in online mode.")

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    try:
        with connectable.connect() as connection:
            context.configure(
                connection=connection,
                target_metadata=Base.metadata,
            )
            with context.begin_transaction():
                logger.info("Running migrations...")
                context.run_migrations()
            logger.info("Migrations completed successfully in online mode.")
    except Exception as e:
        logger.exception(f"An error occurred during online migrations.")
        raise RuntimeError("Failed to run migrations in offline mode.") from e

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
