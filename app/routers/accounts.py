"""
API endpoints for managing user accounts: retrieving, updating, and deleting account info.
Secured with authentication.
"""

from app.config import auth_scheme
from app.database import get_db
from app.schemas import AccountUpdate, AccountOut
from app.services.accounts import AccountService
from fastapi import APIRouter, Depends, status
from fastapi.security.http import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

router = APIRouter(tags=["Account"], prefix="/me")

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=AccountOut,
    summary="Get My Info #",
    description="Retrieve detailed information about the authenticated user. Requires valid authorization credentials.")
def get_my_info(
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> AccountOut:
    "Fetch information about the current user."
    return AccountService.get_my_info(db, token)

@router.put(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=AccountOut,
    summary="Edit My Info #",
    description="Update user information, such as email, password, or other personal details. Requires valid authorization credentials.")
def edit_my_info(
        updated_user: AccountUpdate,
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> AccountOut:
    "Edit the current user's information."
    return AccountService.edit_my_info(db, token, updated_user)

@router.delete(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=AccountOut,
    summary="Delete My Info #",
    description="Delete the current authenticated user's account permanently. Requires valid authorization credentials.")
def remove_my_account(
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> AccountOut:
    "Remove the current user's account."
    return AccountService.remove_my_account(db, token)
