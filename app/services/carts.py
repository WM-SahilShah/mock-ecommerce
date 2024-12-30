from app.config.logging import logger
from app.config.responses import ResponseHandler
from app.config.security import get_current_user
from app.database.models import Cart, CartItem, Product
from app.schemas.carts import CartCreate, CartUpdate
from fastapi import HTTPException, status
from sqlalchemy.orm import Session, joinedload

class CartService:
    "Service for cart-related actions."

    @staticmethod
    def get_all_carts(token: str, db: Session, page: int, limit: int) -> dict:
        "Get all carts."
        logger.info("Retrieving all carts for the user.")
        user_id = get_current_user(token)
        carts = (db.query(Cart)
                .filter(Cart.user_id == user_id)
                .offset((page-1) * limit)
                .limit(limit)
                .all())
        logger.info(f"Successfully retrieved {len(carts)} carts")
        return ResponseHandler.get_all_success(page, limit, "carts", carts)

    @staticmethod
    def get_cart(token: str, db: Session, cart_id: int) -> dict:
        "Get a cart by ID."
        logger.info(f"Retrieving cart with ID {cart_id}.")
        user_id = get_current_user(token)
        cart = (db.query(Cart)
                .filter(Cart.id == cart_id,
                        Cart.user_id == user_id)
                .first())
        if not cart:
            logger.error(f"Cart with ID {cart_id} not found for user {user_id}.")
            ResponseHandler.not_found_error("Cart", cart_id)
        logger.info(f"Successfully retrieved cart with ID {cart.id}.")
        return ResponseHandler.get_single_success("cart", cart_id, cart)

    @staticmethod
    def create_cart(token: str, db: Session, cart: CartCreate) -> dict:
        "Create a new cart"
        logger.info("Creating a new cart.")
        if not cart.cart_items:
            logger.error("Cart creation failed: Empty or incomplete request.")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Cart cannot be empty. Please provide cart items.")
        # Extract cart data
        user_id = get_current_user(token)
        cart_dict = cart.model_dump()
        cart_items_data = cart_dict.pop("cart_items", [])
        cart_items = []
        total_amount = 0
        # Assign a unique cart ID in the 300s
        max_id = (db.query(Cart.id)
                  .filter(Cart.id >= 300)
                  .order_by(Cart.id.desc())
                  .first())
        new_cart_id = max_id.id+1 if max_id else 300
        # Add each product to the cart
        for item_data in cart_items_data:
            product_id = item_data["product_id"]
            quantity = item_data["quantity"]
            product = (db.query(Product)
                       .filter(Product.id == product_id)
                       .first())
            if not product:
                logger.error(f"Product with ID {product_id} not found.")
                return ResponseHandler.not_found_error("Product", product_id)
            subtotal = quantity * product.price * (product.discount_percentage / 100)
            cart_item = CartItem(product_id=product_id, quantity=quantity, subtotal=subtotal)
            total_amount += subtotal
            cart_items.append(cart_item)
        # Create a new Cart instance
        cart_db = Cart(id=new_cart_id, cart_items=cart_items, user_id=user_id, total_amount=total_amount, **cart_dict)
        db.add(cart_db)
        db.commit()
        db.refresh(cart_db)
        logger.info(f"Successfully created cart with ID {cart_db.id}.")
        return ResponseHandler.create_success("Cart", cart_db.id, cart_db)

    @staticmethod
    def update_cart(token: str, db: Session, cart_id: int, updated_cart: CartUpdate) -> dict:
        "Update a cart and its items."
        logger.info(f"Updating cart with ID {cart_id}.")
        # Delete old cart
        user_id = get_current_user(token)
        cart = (db.query(Cart)
                .filter(Cart.id == cart_id,
                        Cart.user_id == user_id)
                .first())
        if not cart:
            logger.error(f"Cart with ID {cart_id} not found for user {user_id}.")
            return ResponseHandler.not_found_error("Cart", cart_id)
        (db.query(CartItem)
         .filter(CartItem.cart_id == cart_id)
         .delete())
        # Add each product to cart
        for item in updated_cart.cart_items:
            product_id = item.product_id
            quantity = item.quantity
            product = (db.query(Product)
                       .filter(Product.id == product_id)
                       .first())
            if not product:
                logger.error(f"Product with ID {product_id} not found.")
                return ResponseHandler.not_found_error("Product", product_id)
            subtotal = quantity * product.price * (product.discount_percentage / 100)
            cart_item = CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity, subtotal=subtotal)
            db.add(cart_item)
        # Add each cart to db
        cart.total_amount = sum(item.subtotal for item in cart.cart_items)
        db.commit()
        db.refresh(cart)
        logger.info(f"Successfully updated cart with ID {cart.id}.")
        return ResponseHandler.update_success("cart", cart.id, cart)

    @staticmethod
    def delete_cart(token: str, db: Session, cart_id: int) -> dict:
        "Delete a cart and its items."
        logger.info(f"Deleting cart with ID {cart_id}.")
        user_id = get_current_user(token)
        cart = (db.query(Cart)
                .options(joinedload(Cart.cart_items)
                        .joinedload(CartItem.product))
                .filter(Cart.id == cart_id,
                        Cart.user_id == user_id)
                .first())
        if not cart:
            logger.error(f"Cart with ID {cart_id} not found for user {user_id}.")
            ResponseHandler.not_found_error("Cart", cart_id)
        for cart_item in cart.cart_items:
            db.delete(cart_item)
        db.delete(cart)
        db.commit()
        logger.info(f"Successfully deleted cart with ID {cart_id}.")
        return ResponseHandler.delete_success("Cart", cart_id, cart)
