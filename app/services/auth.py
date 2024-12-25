from app.config.logging import logger
from app.config.responses import ResponseHandler
from app.config.security import get_password_hash, get_token_payload, get_user_token, verify_password
from app.database.database import get_db
from app.database.models import User
from app.schemas.auth import Signup, TokenResponse
from fastapi import Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class AuthService:
    "Service for authentication-related actions."

    @staticmethod
    async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) -> TokenResponse:
        "Log in a user."
        logger.info(f"Attempting login for username: {user_credentials.username}")
        user = (db.query(User)
                .filter(User.username == user_credentials.username)
                .first())
        if not user:
            logger.error(f"Login failed: No such username exists for {user_credentials.username}.")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such username exists.")
        if not verify_password(user_credentials.password, user.password):
            logger.error(f"Login failed: Incorrect password for {user_credentials.username}.")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password.")
        logger.info(f"User {user_credentials.username} logged in successfully.")
        return await get_user_token(id=user.id)

    @staticmethod
    async def signup(db: Session, user: Signup) -> dict:
        "Sign up a new user."
        logger.info(f"Attempting to sign up user: {user.username}")
        existing_user = (db.query(User)
                         .filter(User.username == user.username)
                         .first())
        if existing_user:
            logger.error(f"Signup failed: Username {user.username} already exists.")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists.")
        hashed_password = get_password_hash(user.password)
        user.password = hashed_password
        db_user = User(id=None, **user.model_dump())
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
            raise ResponseHandler.invalid_token("refresh")
        user = (db.query(User)
                .filter(User.id == user_id)
                .first())
        if not user:
            logger.error(f"Refresh token is invalid: No user found with ID {user_id}.")
            raise ResponseHandler.invalid_token("refresh")
        logger.info(f"Refresh token issued successfully for user ID: {user.id}.")
        return await get_user_token(id=user.id, refresh_token=token)
