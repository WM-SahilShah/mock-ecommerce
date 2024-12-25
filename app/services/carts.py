from app.database.models import Cart, CartItem, Product
from app.core.responses import ResponseHandler
from app.schemas.carts import CartCreate, CartUpdate
from app.core.security import get_current_user
from sqlalchemy.orm import Session, joinedload

class CartService:
    "Service for cart-related actions."

    @staticmethod
    def get_all_carts(token: str, db: Session, page: int, limit: int) -> dict:
        "Get all carts."
        user_id = get_current_user(token)
        carts = db.query(Cart).filter(Cart.user_id == user_id).offset((page - 1) * limit).limit(limit).all()
        message = f"Page {page} with {limit} carts"
        return ResponseHandler.success(message, carts)

    @staticmethod
    def get_cart(token: str, db: Session, cart_id: int) -> dict:
        "Get a cart by ID."
        user_id = get_current_user(token)
        cart = db.query(Cart).filter(Cart.id == cart_id, Cart.user_id == user_id).first()
        if not cart:
            ResponseHandler.not_found_error("Cart", cart_id)
        return ResponseHandler.get_single_success("cart", cart_id, cart)

    @staticmethod
    def create_cart(token: str, db: Session, cart: CartCreate) -> dict:
        "Create a new cart."
        user_id = get_current_user(token)
        cart_dict = cart.model_dump()
        cart_items_data = cart_dict.pop("cart_items", [])
        cart_items = []
        total_amount = 0
        for item_data in cart_items_data:
            product_id = item_data["product_id"]
            quantity = item_data["quantity"]
            product = db.query(Product).filter(Product.id == product_id).first()
            if not product:
                return ResponseHandler.not_found_error("Product", product_id)
            subtotal = quantity * product.price * (product.discount_percentage / 100)
            cart_item = CartItem(product_id=product_id, quantity=quantity, subtotal=subtotal)
            total_amount += subtotal
            cart_items.append(cart_item)
        cart_db = Cart(cart_items=cart_items, user_id=user_id, total_amount=total_amount, **cart_dict)
        db.add(cart_db)
        db.commit()
        db.refresh(cart_db)
        return ResponseHandler.create_success("Cart", cart_db.id, cart_db)

    @staticmethod
    def update_cart(token: str, db: Session, cart_id: int, updated_cart: CartUpdate) -> dict:
        "Update a cart and its items."
        user_id = get_current_user(token)
        cart = db.query(Cart).filter(Cart.id == cart_id, Cart.user_id == user_id).first()
        if not cart:
            return ResponseHandler.not_found_error("Cart", cart_id)
        db.query(CartItem).filter(CartItem.cart_id == cart_id).delete()
        for item in updated_cart.cart_items:
            product_id = item.product_id
            quantity = item.quantity
            product = db.query(Product).filter(Product.id == product_id).first()
            if not product:
                return ResponseHandler.not_found_error("Product", product_id)
            subtotal = quantity * product.price * (product.discount_percentage / 100)
            cart_item = CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity, subtotal=subtotal)
            db.add(cart_item)
        cart.total_amount = sum(item.subtotal for item in cart.cart_items)
        db.commit()
        db.refresh(cart)
        return ResponseHandler.update_success("cart", cart.id, cart)

    @staticmethod
    def delete_cart(token: str, db: Session, cart_id: int) -> dict:
        "Delete a cart and its items."
        user_id = get_current_user(token)
        cart = db.query(Cart).options(joinedload(Cart.cart_items).joinedload(CartItem.product)).filter(
            Cart.id == cart_id, Cart.user_id == user_id).first()
        if not cart:
            ResponseHandler.not_found_error("Cart", cart_id)
        for cart_item in cart.cart_items:
            db.delete(cart_item)
        db.delete(cart)
        db.commit()
        return ResponseHandler.delete_success("Cart", cart_id, cart)
