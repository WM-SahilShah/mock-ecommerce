"""
This module contains routes for managing categories, including retrieving all categories, creating a new category, updating an existing category, and deleting a category. Some endpoints are restricted to admins.
"""

from app.config import check_admin_role
from app.database import get_db
from app.schemas import CategoryCreate, CategoryOut, CategoriesOut, CategoryOutDelete, CategoryUpdate
from app.services import CategoryService
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session


router = APIRouter(tags=["Categories"], prefix="/categories")


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=CategoriesOut,
    summary="Get All Categories",
    description="This endpoint retrieves a paginated list of all categories with an optional search parameter to filter by category name.")
def get_all_categories(
        db: Session = Depends(get_db),
        page: int = Query(1, ge=1, description="Page number (Required)"),
        limit: int = Query(10, ge=1, le=100, description="Items per page (Required)"),
        search: str = Query("", description="Search based name of categories"),
    ) -> CategoriesOut:
    "Retrieve all categories with pagination and optional search by name."
    return CategoryService.get_all_categories(db, page, limit, search)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoryOut,
    dependencies=[Depends(check_admin_role)],
    summary="Create New Category ##",
    description="This endpoint allows an admin to create a new category.")
def create_category(
        category: CategoryCreate,
        db: Session = Depends(get_db)
    ) -> CategoryOut:
    "Create a new category."
    return CategoryService.create_category(db, category)


@router.get(
    "/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=CategoryOut,
    summary="Get Specific Category",
    description="This endpoint retrieves a specific category by its ID.")
def get_category(
        category_id: int,
        db: Session = Depends(get_db)
    ) -> CategoryOut:
    "Retrieve a specific category by its ID."
    return CategoryService.get_category(db, category_id)


@router.put(
    "/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=CategoryOut,
    dependencies=[Depends(check_admin_role)],
    summary="Update Existing category ##",
    description="This endpoint allows an admin to update an existing category by its ID.")
def update_category(
        category_id: int,
        updated_category: CategoryUpdate,
        db: Session = Depends(get_db)
    ) -> CategoryOut:
    "Update an existing category by its ID."
    return CategoryService.update_category(db, category_id, updated_category)


@router.delete(
    "/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=CategoryOutDelete,
    dependencies=[Depends(check_admin_role)],
    summary="Delete Existing Category ##",
    description="This endpoint allows an admin to delete a category by its ID.")
def delete_category(
        category_id: int,
        db: Session = Depends(get_db)
    ) -> CategoryOutDelete:
    "Delete a category by its ID."
    return CategoryService.delete_category(db, category_id)
