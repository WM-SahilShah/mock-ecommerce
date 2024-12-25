from typing import Generator
from app.core.settings import DB_URL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Establish a connection to the PostgreSQL database
engine = create_engine(DB_URL)

# Create database tables based on the defined SQLAlchemy models (subclasses of the Base class)
Base = declarative_base()

# Connect to the database and provide a session for interacting with it
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
