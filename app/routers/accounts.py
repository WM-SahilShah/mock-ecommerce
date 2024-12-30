from app.config.security import auth_scheme
from app.database.database import get_db
from app.schemas.accounts import AccountUpdate
from app.schemas.users import UserOut
from app.services.accounts import AccountService
from fastapi import APIRouter, Depends
from fastapi.security.http import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

router = APIRouter(tags=["Account"], prefix="/me")

@router.get("/", response_model=UserOut)
def get_my_info(
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> UserOut:
    "Fetch information about the current user."
    return AccountService.get_my_info(db, token)

@router.put("/", response_model=UserOut)
def edit_my_info(
        updated_user: AccountUpdate,
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> UserOut:
    "Edit the current user's information."
    return AccountService.edit_my_info(db, token, updated_user)

@router.delete("/", response_model=UserOut)
def remove_my_account(
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> UserOut:
    "Remove the current user's account."
    return AccountService.remove_my_account(db, token)
