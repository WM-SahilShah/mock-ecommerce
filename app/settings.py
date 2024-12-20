from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database variables
DB_URL = os.getenv("DB_URL")

# JWT variables
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 1))  #Default to 0 if not set
ALGORITHM = os.getenv("ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")
