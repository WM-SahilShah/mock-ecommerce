from app.database import get_db
from app.services.carts import CartService
from app.schemas.carts import CartCreate, CartUpdate, CartOut, CartOutDelete, CartsOutList
from fastapi import APIRouter, Depends, Query, status
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

router = APIRouter(tags=["Carts"], prefix="/carts")
auth_scheme = HTTPBearer()

@router.get("/", status_code=status.HTTP_200_OK, response_model=CartsOutList)
def get_all_carts(
        db: Session = Depends(get_db),
        page: int = Query(1, ge=1, description="Page number"),
        limit: int = Query(10, ge=1, le=100, description="Items per page"),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> CartsOutList:
    "Retrieve all carts with pagination."
    return CartService.get_all_carts(token, db, page, limit)

@router.get("/{cart_id}", status_code=status.HTTP_200_OK, response_model=CartOut)
def get_cart(
        cart_id: int,
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> CartOut:
    "Retrieve a specific cart by its ID."
    return CartService.get_cart(token, db, cart_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CartOut)
def create_cart(
        cart: CartCreate, db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> CartOut:
    "Create a new cart."
    return CartService.create_cart(token, db, cart)

@router.put("/{cart_id}", status_code=status.HTTP_200_OK, response_model=CartOut)
def update_cart(
        cart_id: int,
        updated_cart: CartUpdate,
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> CartOut:
    "Update an existing cart."
    return CartService.update_cart(token, db, cart_id, updated_cart)

@router.delete("/{cart_id}", status_code=status.HTTP_200_OK, response_model=CartOutDelete)
def delete_cart(
        cart_id: int, db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
    ) -> CartOutDelete:
    "Delete a cart by its ID."
    return CartService.delete_cart(token, db, cart_id)
