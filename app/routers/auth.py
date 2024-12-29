from app.database.database import get_db
from app.schemas.auth import TokenResponse, UserOut, Signup
from app.services.auth import AuthService
from fastapi import APIRouter, Depends, status, Header
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(tags=["Auth"], prefix="/auth")

@router.post("/signup", status_code=status.HTTP_200_OK, response_model=UserOut)
async def user_signup(
        user: Signup,
        db: Session = Depends(get_db)
    ) -> UserOut:
    "Sign up a new user."
    return await AuthService.signup(db, user)


@router.post("/login", status_code=status.HTTP_200_OK, response_model=TokenResponse)
async def user_login(
        user_credentials: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
    ) -> TokenResponse:
    "Login an existing user."
    return await AuthService.login(user_credentials, db)

@router.post("/refresh", status_code=status.HTTP_200_OK, response_model=TokenResponse)
async def refresh_access_token(
        refresh_token: str = Header(),
        db: Session = Depends(get_db)
    ) -> TokenResponse:
    "Refresh the user's access token."
    return await AuthService.get_refresh_token(token=refresh_token, db=db)
