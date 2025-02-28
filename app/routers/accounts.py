"""
API endpoints for managing user accounts: retrieving, updating, and deleting account info.
Secured with authentication.
"""

from app.config import auth_scheme
from app.database import get_db
from app.schemas import AccountUpdate, AccountOut
from app.services import AccountService
from fastapi import APIRouter, Depends, status
from fastapi.security.http import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

router = APIRouter(tags=["Account"], prefix="/me")

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=AccountOut,
    summary="Get My Info #",
    description="This endpoint uses the authorization credentials to retrieve detailed information about the user.")
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
    description="This endpoint allows the user to update their stored information.")
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
    description="This endpoint allows the user to delete their account permanently.")
def remove_my_account(
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> AccountOut:
    "Remove the current user's account."
    return AccountService.remove_my_account(db, token)
