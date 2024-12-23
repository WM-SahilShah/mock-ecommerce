from app.database import get_db
from app.security import check_admin_role
from app.services.users import UserService
from app.schemas.users import UserCreate, UserOut, UsersOut, UserOutDelete, UserUpdate
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

router = APIRouter(tags=["Users"], prefix="/users")

@router.get("/", status_code=status.HTTP_200_OK, response_model=UsersOut, dependencies=[Depends(check_admin_role)])
def get_all_users(
        db: Session = Depends(get_db),
        page: int = Query(1, ge=1, description="Page number"),
        limit: int = Query(10, ge=1, le=100, description="Items per page"),
        search: str | None = Query("", description="Search by username"),
        role: str = Query("user", enum=["user", "admin"])
    ) -> UsersOut:
    "Retrieve all users with pagination, search, and role filtering."
    return UserService.get_all_users(db, page, limit, search, role)

@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserOut, dependencies=[Depends(check_admin_role)])
def get_user(
        user_id: int,
        db: Session = Depends(get_db)
    ) -> UserOut:
    "Retrieve a specific user by their ID."
    return UserService.get_user(db, user_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut, dependencies=[Depends(check_admin_role)])
def create_user(
        user: UserCreate,
        db: Session = Depends(get_db)
    ) -> UserOut:
    "Create a new user."
    return UserService.create_user(db, user)

@router.put("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserOut, dependencies=[Depends(check_admin_role)])
def update_user(
        user_id: int,
        updated_user: UserUpdate,
        db: Session = Depends(get_db)
    ) -> UserOut:
    "Update an existing user by their ID."
    return UserService.update_user(db, user_id, updated_user)

@router.delete("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserOutDelete, dependencies=[Depends(check_admin_role)])
def delete_user(
        user_id: int,
        db: Session = Depends(get_db)
    ) -> UserOutDelete:
    "Delete a user by their ID."
    return UserService.delete_user(db, user_id)
