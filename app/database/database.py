"""
This module handles database connectivity and session management using SQLAlchemy.
"""

from app.config import logger, DB_URL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator

# Establish a connection to the PostgreSQL database
engine = create_engine(DB_URL)

# Create database tables based on the defined SQLAlchemy models (subclasses of the Base class)
Base = declarative_base()

# Connect to the database and provide a session for interacting with it
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    "Provides a session for interacting with the database."
    try:
        db = SessionLocal()
        logger.info("Database session started.")
        yield db
    except Exception as e:
        logger.exception("An error occurred while interacting with the database.")
        raise e
    finally:
        db.close()
        logger.info("Database session closed.")
