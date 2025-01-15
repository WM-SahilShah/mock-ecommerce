"""
This module loads and manages application configuration settings from environment variables.
It supports database configurations, JWT settings, and other application-specific parameters.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database variables
DB_URL = os.getenv("DB_URL")

# JWT variables
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 1))  # Default: 1
ALGORITHM = os.getenv("ALGORITHM", "HS256")  # Default: HS256
SECRET_KEY = os.getenv("SECRET_KEY")
