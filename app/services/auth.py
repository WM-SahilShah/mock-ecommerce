from app.database import get_db
from app.models import User
from app.responses import ResponseHandler
from app.schemas.auth import Signup
from app.security import get_password_hash, get_token_payload, get_user_token, verify_password
from fastapi import Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class AuthService:
    "Service for authentication-related actions."

    @staticmethod
    async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) -> dict:
        "Log in a user."
        user = db.query(User).filter(User.username == user_credentials.username).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
        if not verify_password(user_credentials.password, user.password):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
        return await get_user_token(id=user.id)

    @staticmethod
    async def signup(db: Session, user: Signup) -> dict:
        "Sign up a new user."
        hashed_password = get_password_hash(user.password)
        user.password = hashed_password
        db_user = User(id=None, **user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return ResponseHandler.create_success(db_user.username, db_user.id, db_user)

    @staticmethod
    async def get_refresh_token(token: str, db: Session) -> dict:
        "Get a new refresh token."
        payload = get_token_payload(token)
        user_id = payload.get("id", None)
        if not user_id:
            raise ResponseHandler.invalid_token("refresh")
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ResponseHandler.invalid_token("refresh")
        return await get_user_token(id=user.id, refresh_token=token)
