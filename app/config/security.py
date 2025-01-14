"""
This module handles authentication and authorization for the application. 

Features:
- Password hashing and verification.
- JWT token creation and validation.
- User extraction from tokens.
- Role-based access control.
"""

from app.config import logger, ResponseHandler, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
from app.database import get_db, User
from app.schemas.auth import TokenResponse
from datetime import datetime, timedelta, timezone
from fastapi import Depends
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

# Password Hashing Context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
auth_scheme = HTTPBearer()

# Create Hash Password
def get_password_hash(password: str) -> str:
    "Hash a plain text password using bcrypt."
    logger.info("Hashing password.")
    return pwd_context.hash(password)

# Verify Hash Password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    "Verify if the plain password matches the hashed password."
    logger.info("Verifying password.")
    return pwd_context.verify(plain_password, hashed_password)

# Create Access & Refresh Token
async def get_user_token(id: int, refresh_token: str = None) -> TokenResponse:
    "Generate access and refresh tokens for a user."
    logger.info(f"Generating tokens for user ID {id}.")
    payload = {"id": id}
    access_token_expiry = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await create_access_token(payload, access_token_expiry)

    if not refresh_token:
        refresh_token = await create_refresh_token(payload)

    logger.info(f"Tokens generated successfully for user ID {id}.")
    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=access_token_expiry.seconds
    )

# Create Access Token
async def create_access_token(data: dict, access_token_expiry: timedelta) -> str:
    "Create a JWT access token for a given payload."
    logger.info("Creating access token.")
    payload = data.copy()
    expire = datetime.now(timezone.utc) + access_token_expiry
    payload.update({"exp": expire})

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    logger.info("Access token created successfully.")
    return token

# Create Refresh Token
async def create_refresh_token(data: dict) -> str:
    "Create a JWT refresh token for a given payload."
    logger.info("Creating refresh token.")
    return jwt.encode(data, SECRET_KEY, ALGORITHM)

# Get Payload Of Token
def get_token_payload(token: str) -> dict:
    "Decode and return the payload of a JWT token if valid else, raises `JWTError`"
    try:
        logger.info("Decoding token payload.")
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        logger.error("Failed to decode token: Invalid token.")
        raise ResponseHandler.invalid_credentials("Invalid access token")

# Get Current User from Token
def get_current_user(token: HTTPAuthorizationCredentials) -> int:
    "Extract the current user's ID from the token."
    logger.info("Extracting user ID from token.")
    user = get_token_payload(token.credentials)
    return user.get('id')

# Check if User has Admin Role
def check_admin_role(
        token: HTTPAuthorizationCredentials = Depends(auth_scheme),
        db: Session = Depends(get_db)) -> None:
    "Verify if the user associated with the token has an admin role."
    logger.info("Checking admin role for user.")
    user = get_token_payload(token.credentials)
    user_id = user.get('id')
    role_user = (db.query(User)
                 .filter(User.id == user_id)
                 .first())

    if role_user is None:
        logger.error(f"User ID {user_id} not found.")
        raise ResponseHandler.not_found_error(f"User with id {user_id}")

    if role_user.role != "admin":
        logger.error(f"User ID {user_id} does not have admin role.")
        raise ResponseHandler.restricted_access()
    
    logger.info(f"User ID {user_id} has admin role.")