"""
This module defines API routes for managing users, including retrieving, creating, updating, and deleting users.
It also supports pagination, search, and role-based filtering. All user-related actions require admin role authorization.
"""

from app.config.security import check_admin_role
from app.database.database import get_db
from app.schemas import UserCreate, UserOut, UsersOut, UserOutDelete, UserUpdate
from app.services.users import UserService
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

router = APIRouter(tags=["Users"], prefix="/users")

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=UsersOut,
    dependencies=[Depends(check_admin_role)],
    summary="Get All Users ##",
    description="This endpoint retrieves all users with pagination (required), search by username (optional), and role filtering (optional).")
def get_all_users(
        db: Session = Depends(get_db),
        page: int = Query(1, ge=1, description="Page number (Required)"),
        limit: int = Query(10, ge=1, le=100, description="Items per page (Required)"),
        search: str = Query("", description="Search by username"),
        role: str = Query("", enum=["user", "admin", ""], description="Filter by user role (Optional)")
    ) -> UsersOut:
    "Retrieve all users with pagination, search, and role filtering."
    return UserService.get_all_users(db, page, limit, search, role)

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserOut,
    dependencies=[Depends(check_admin_role)],
    summary="Create New User ##",
    description="This endpoint allows an admin to create a new user.")
def create_user(
        user: UserCreate,
        db: Session = Depends(get_db)
    ) -> UserOut:
    "Create a new user."
    return UserService.create_user(db, user)

@router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserOut,
    dependencies=[Depends(check_admin_role)],
    summary="Get Specific User ##",
    description="This endpoint retrieves a specific user by their ID.")
def get_user(
        user_id: int,
        db: Session = Depends(get_db)
    ) -> UserOut:
    "Retrieve a specific user by their ID."
    return UserService.get_user(db, user_id)


@router.put(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserOut,
    dependencies=[Depends(check_admin_role)],
    summary="Update User by ID",
    description="This endpoint allows an admin to update an existing user by their ID.")
def update_user(
        user_id: int,
        updated_user: UserUpdate,
        db: Session = Depends(get_db)
    ) -> UserOut:
    "Update an existing user by their ID."
    return UserService.update_user(db, user_id, updated_user)

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserOutDelete,
    dependencies=[Depends(check_admin_role)],
    summary="Delete User by ID",
    description="This endpoint allows an admin to delete a user by their ID.")
def delete_user(
        user_id: int,
        db: Session = Depends(get_db)
    ) -> UserOutDelete:
    "Delete a user by their ID."
    return UserService.delete_user(db, user_id)
