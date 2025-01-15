"""
This module contains routes for managing carts, including retrieving all carts, creating a new cart, updating an existing cart, and deleting a cart. The endpoints support authentication through a token.
"""

from app.config import auth_scheme
from app.database import get_db
from app.schemas import CartCreate, CartUpdate, CartOut, CartOutDelete, CartsOut
from app.services import CartService
from fastapi import APIRouter, Depends, Query, status
from fastapi.security.http import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session


router = APIRouter(tags=["Carts"], prefix="/carts")


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=CartsOut,
    summary="Get All Carts #",
    description="This endpoint retrieves a paginated list of all carts for the particular user.")
def get_all_carts(
        db: Session = Depends(get_db),
        page: int = Query(1, ge=1, description="Page number (Required)"),
        limit: int = Query(10, ge=1, le=100, description="Items per page (Required)"),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> CartsOut:
    "Retrieve all carts with pagination."
    return CartService.get_all_carts(token, db, page, limit)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=CartOut,
    summary="Create New Cart #",
    description="This endpoint creates a new cart for the user.")
def create_cart(
        cart: CartCreate,
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> CartOut:
    "Create a new cart."
    return CartService.create_cart(token, db, cart)


@router.get(
    "/{cart_id}",
    status_code=status.HTTP_200_OK,
    response_model=CartOut,
    summary="Get Specific Cart #",
    description="This endpoint retrieves a specific cart by its ID.")
def get_cart(
        cart_id: int,
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> CartOut:
    "Retrieve a specific cart by its ID."
    return CartService.get_cart(token, db, cart_id)


@router.put(
    "/{cart_id}",
    status_code=status.HTTP_200_OK,
    response_model=CartOut,
    summary="Update Existing Cart #",
    description="This endpoint updates an existing cart by its ID.")
def update_cart(
        cart_id: int,
        updated_cart: CartUpdate,
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> CartOut:
    "Update an existing cart."
    return CartService.update_cart(token, db, cart_id, updated_cart)


@router.delete(
    "/{cart_id}",
    status_code=status.HTTP_200_OK,
    response_model=CartOutDelete,
    summary="Delete Existing Cart #",
    description="This endpoint deletes a cart by its ID.")
def delete_cart(
        cart_id: int,
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> CartOutDelete:
    "Delete a cart by its ID."
    return CartService.delete_cart(token, db, cart_id)
