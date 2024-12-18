from app.database import get_db
from app.security import auth_scheme
from app.services.accounts import AccountService
from app.schemas.accounts import AccountOut, AccountUpdate
from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

router = APIRouter(tags=["Account"], prefix="/me")
auth_scheme = HTTPBearer()

@router.get("/", response_model=AccountOut)
def get_my_info(
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> AccountOut:
    "Fetch information about the current user."
    return AccountService.get_my_info(db, token)

@router.put("/", response_model=AccountOut)
def edit_my_info(
        updated_user: AccountUpdate,
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> AccountOut:
    "Edit the current user's information."
    return AccountService.edit_my_info(db, token, updated_user)

@router.delete("/", response_model=AccountOut)
def remove_my_account(
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> AccountOut:
    "Remove the current user's account."
    return AccountService.remove_my_account(db, token)
