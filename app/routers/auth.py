"""
This module contains routes related to user authentication, including signing up a new user, logging in an existing user, and refreshing the access token using a refresh token.
"""

from app.database import get_db
from app.schemas import TokenResponse, UserCreate, UserOut
from app.services import AuthService
from fastapi import APIRouter, Depends, status, Header
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(tags=["Auth"], prefix="/auth")

@router.post(
    "/signup",
    status_code=status.HTTP_201_CREATED,
    response_model=UserOut,
    summary="User Signup",
    description="This endpoint allows a user to create a new account by providing the necessary details.")
async def user_signup(
        user: UserCreate,
        db: Session = Depends(get_db)
    ) -> UserOut:
    "Sign up a new user."
    return await AuthService.signup(db, user)


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=TokenResponse,
    summary="User Login",
    description="This endpoint allows an existing user to log in using their credentials and receive an access token.")
async def user_login(
        user_credentials: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
    ) -> TokenResponse:
    "Login an existing user."
    return await AuthService.login(user_credentials, db)


@router.post(
    "/refresh",
    status_code=status.HTTP_200_OK,
    response_model=TokenResponse,
    summary="Refresh Access Token",
    description="This endpoint allows the user to refresh their access token using a valid refresh token.")
async def refresh_access_token(
        refresh_token: str = Header(),
        db: Session = Depends(get_db)
    ) -> TokenResponse:
    "Refresh the user's access token."
    return await AuthService.get_refresh_token(token=refresh_token, db=db)
