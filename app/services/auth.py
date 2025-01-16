"""
This module provides the AuthService class for handling authentication-related actions, 
such as user login, signup, and token refresh functionality.
"""

from app.config import logger, ResponseHandler, get_password_hash, get_token_payload, get_user_token, verify_password
from app.database import get_db, User
from app.schemas import TokenResponse, UserCreate, CustomOAuth2PasswordRequestForm
from fastapi import Depends
from sqlalchemy.orm import Session

class AuthService:
    """
    Service class for authentication-related actions.

    Methods:
        `login(user_credentials, db)`: Log in a user and return an access token.
        `signup(db, user)`: Sign up a new user and store their information in the database.
        `get_refresh_token(token, db)`: Generate a new access token using a refresh token.
    """

    @staticmethod
    async def login(user_credentials: CustomOAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) -> TokenResponse:
        "Log a user in."
        logger.info(f"Attempting login for username: {user_credentials.username}")
        user = (db.query(User)
                .filter(User.username == user_credentials.username)
                .first())
        if not user:
            logger.error(f"Login failed: No such username exists for {user_credentials.username}.")
            raise ResponseHandler.not_found_error(f"User with username {user_credentials.username}")
        if not verify_password(user_credentials.password, user.password):
            logger.error(f"Login failed: Incorrect password for {user_credentials.username}.")
            raise ResponseHandler.invalid_credentials("Incorrect username or password.")
        logger.info(f"User {user_credentials.username} logged in successfully.")
        return await get_user_token(id=user.id)

    @staticmethod
    async def signup(db: Session, user: UserCreate) -> dict:
        "Sign a new user up."
        logger.info(f"Attempting to sign up user: {user.username}")
        if not user.username or not user.password or not user.email:
            logger.error("Signup failed: Missing required fields.")
            raise ResponseHandler.malformed_request("Missing required fields: username, password, and/or email")
        existing_user = (db.query(User)
                         .filter(User.username == user.username)
                         .first())
        if existing_user:
            logger.error(f"Signup failed: Username {user.username} already exists.")
            raise ResponseHandler.malformed_request("User already exists.")
        hashed_password = get_password_hash(user.password)
        user.password = hashed_password
        max_id = (db.query(User.id)
                  .filter(User.id >= 500)
                  .order_by(User.id.desc())
                  .first())
        new_user_id = max_id.id+1 if max_id else 500
        db_user = User(id=new_user_id, **user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logger.info(f"User {user.username} signed up successfully with ID: {db_user.id}")
        return ResponseHandler.create_success(db_user.username, db_user.id, db_user)

    @staticmethod
    async def get_refresh_token(token: str, db: Session) -> TokenResponse:
        "Get a new refresh token."
        logger.info("Attempting to refresh token.")
        payload = get_token_payload(token)
        user_id = payload.get("id", None)
        if not user_id:
            logger.error("Refresh token is invalid: No user ID found in token.")
            raise ResponseHandler.invalid_credentials("Invalid refresh token")
        user = (db.query(User)
                .filter(User.id == user_id)
                .first())
        if not user:
            logger.error(f"Refresh token is invalid: No user found with ID {user_id}.")
            raise ResponseHandler.invalid_credentials("Invalid refresh token")
        logger.info(f"Refresh token issued successfully for user ID: {user.id}.")
        return await get_user_token(id=user.id, refresh_token=token)
