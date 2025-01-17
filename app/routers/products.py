"""
This module defines the API routes for managing products, including retrieving, creating, updating, and deleting products.
The routes support pagination, searching, and role-based access control.
"""

from app.config import check_admin_role
from app.database import get_db
from app.schemas import ProductCreate, ProductOut, ProductsOut, ProductOutDelete, ProductUpdate
from app.services import ProductService
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session


router = APIRouter(tags=["Products"], prefix="/products")


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=ProductsOut,
    summary="Get All Products",
    description="This endpoint retrieves all products with pagination (required) and search by title (optional).")
def get_all_products(
        db: Session = Depends(get_db),
        page: int = Query("<integer>*", ge=1, description="Page number (Required)"),
        limit: int = Query("<integer>*", ge=1, le=100, description="Items per page (Required)"),
        search: str = Query("{{searchQuery}}", description="Search based title of products"),
    ) -> ProductsOut:
    "Retrieve all products with pagination and optional search by title."
    return ProductService.get_all_products(db, page, limit, search)


@router.post(
    "/", 
    status_code=status.HTTP_201_CREATED, 
    response_model=ProductOut, 
    dependencies=[Depends(check_admin_role)],
    summary="Create New Product ##",
    description="This endpoint allows an admin to create a new product.")
def create_product(
        product: ProductCreate,
        db: Session = Depends(get_db)
    ) -> ProductOut:
    "Create a new product."
    return ProductService.create_product(db, product)


@router.get(
    "/{product_id}", 
    status_code=status.HTTP_200_OK, 
    response_model=ProductOut,
    summary="Get Specific Product",
    description="This endpoint retrieves a specific product by its ID.")
def get_product(
        product_id: int,
        db: Session = Depends(get_db)
    ) -> ProductOut:
    "Retrieve a specific product by its ID."
    return ProductService.get_product(db, product_id)


@router.put(
    "/{product_id}",
    status_code=status.HTTP_200_OK,
    response_model=ProductOut,
    dependencies=[Depends(check_admin_role)],
    summary="Update Existing Product ##",
    description="This endpoint allows an admin to update an existing product by its ID.")
def update_product(
        product_id: int,
        updated_product: ProductUpdate,
        db: Session = Depends(get_db)
    ) -> ProductOut:
    "Update an existing product by its ID."
    return ProductService.update_product(db, product_id, updated_product)


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_200_OK,
    response_model=ProductOutDelete,
    dependencies=[Depends(check_admin_role)],
    summary="Delete Existing Category ##",
    description="This endpoint allows an admin to delete an existing product by its ID.")
def delete_product(
        product_id: int,
        db: Session = Depends(get_db)
    ) -> ProductOutDelete:
    "Delete a product by its ID."
    return ProductService.delete_product(db, product_id)
