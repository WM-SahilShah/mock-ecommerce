from app.database import get_db
from app.security import check_admin_role
from app.services.categories import CategoryService
from app.schemas.categories import CategoryCreate, CategoryOut, CategoriesOut, CategoryOutDelete, CategoryUpdate
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

router = APIRouter(tags=["Categories"], prefix="/categories")

@router.get("/", status_code=status.HTTP_200_OK, response_model=CategoriesOut)
def get_all_categories(
        db: Session = Depends(get_db),
        page: int = Query(1, ge=1, description="Page number"),
        limit: int = Query(10, ge=1, le=100, description="Items per page"),
        search: str | None = Query("", description="Search based name of categories"),
    ) -> CategoriesOut:
    "Retrieve all categories with pagination and optional search by name."
    return CategoryService.get_all_categories(db, page, limit, search)

@router.get("/{category_id}", status_code=status.HTTP_200_OK, response_model=CategoryOut)
def get_category(
        category_id: int,
        db: Session = Depends(get_db)
    ) -> CategoryOut:
    "Retrieve a specific category by its ID."
    return CategoryService.get_category(db, category_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CategoryOut, dependencies=[Depends(check_admin_role)])
def create_category(
        category: CategoryCreate,
        db: Session = Depends(get_db)
    ) -> CategoryOut:
    "Create a new category."
    return CategoryService.create_category(db, category)

@router.put("/{category_id}", status_code=status.HTTP_200_OK, response_model=CategoryOut, dependencies=[Depends(check_admin_role)])
def update_category(
        category_id: int,
        updated_category: CategoryUpdate,
        db: Session = Depends(get_db)
    ) -> CategoryOut:
    "Update an existing category by its ID."
    return CategoryService.update_category(db, category_id, updated_category)

@router.delete("/{category_id}", status_code=status.HTTP_200_OK, response_model=CategoryOutDelete, dependencies=[Depends(check_admin_role)])
def delete_category(
        category_id: int,
        db: Session = Depends(get_db)
    ) -> CategoryOutDelete:
    "Delete a category by its ID."
    return CategoryService.delete_category(db, category_id)
