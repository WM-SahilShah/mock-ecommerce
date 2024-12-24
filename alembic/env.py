from alembic import context
from app.database import Base
from app.settings import DB_URL
from app.models import User, Cart, CartItem, Product
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool

# Access Alembic configuration
config = context.config
config.set_main_option("sqlalchemy.url", DB_URL)
if config.config_file_name:
    fileConfig(config.config_file_name)

def run_migrations_offline() -> None:
    """Run migrations in `offline` mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=Base.metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in `online` mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=Base.metadata
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
