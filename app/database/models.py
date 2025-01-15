"""
models.py
=========
This module defines the SQLAlchemy ORM models for the application's database tables.
Models: User, Cart, CartItem, Category, Product.
"""

from .database import Base
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Float, ARRAY, Enum
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship


class User(Base):
    """
    Represents a user in the system.

    Attributes:
    - `id` (int): Primary key, unique identifier for the user.
    - `username` (str): Unique username of the user.
    - `email` (str): Unique email address of the user.
    - `password` (str): Hashed password of the user.
    - `full_name` (str): Full name of the user.
    - `is_active` (bool): Indicates if the user account is active.
    - `role` (str): Role of the user, either 'admin' or 'user'.
    - `created_at` (datetime): Timestamp of user creation.
    
    Relationships:
    - `carts`: One-to-many relationship with the Cart model.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    is_active = Column(Boolean, server_default="True", nullable=False)
    role = Column(Enum("admin", "user", name="user_roles"), nullable=False, server_default="user")
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"), nullable=False)

    # Relationships
    carts = relationship("Cart", back_populates="user")


class Cart(Base):
    """
    Represents a shopping cart for a user.

    Attributes:
    - `id` (int): Primary key, unique identifier for the cart.
    - `user_id` (int): Foreign key referencing the User model.
    - `created_at` (datetime): Timestamp of cart creation.
    - `total_amount` (float): Total amount of the cart.
    
    Relationships:
    - `user`: Many-to-one relationship with the User model.
    - `cart_items`: One-to-many relationship with the CartItem model.
    """
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"), nullable=False)
    total_amount = Column(Float, nullable=False)

    # Relationships
    user = relationship("User", back_populates="carts")
    cart_items = relationship("CartItem", back_populates="cart")


class CartItem(Base):
    """
    Represents an item in a shopping cart.

    Attributes:
    - `id` (int): Primary key, unique identifier for the cart item.
    - `cart_id` (int): Foreign key referencing the Cart model.
    - `product_id` (int): Foreign key referencing the Product model.
    - `quantity` (int): Quantity of the product in the cart.
    - `subtotal` (float): Subtotal price for the item (quantity * price).
    
    Relationships:
    - `cart`: Many-to-one relationship with the Cart model.
    - `product`: Many-to-one relationship with the Product model.
    """
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey("carts.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False)
    subtotal = Column(Float, nullable=False)

    # Relationships
    cart = relationship("Cart", back_populates="cart_items")
    product = relationship("Product", back_populates="cart_items")


class Category(Base):
    """
    Represents a product category.

    Attributes:
    - `id` (int): Primary key, unique identifier for the category.
    - `name` (str): Name of the category.
    
    Relationships:
    - `products`: One-to-many relationship with the Product model.
    """
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)

    # Relationships
    products = relationship("Product", back_populates="category")


class Product(Base):
    """
    Represents a product available for purchase.

    Attributes:
    - `id` (int): Primary key, unique identifier for the product.
    - `title` (str): Title of the product.
    - `description` (str): Description of the product.
    - `price` (int): Price of the product in the smallest currency unit (e.g., cents).
    - `discount_percentage` (float): Discount percentage on the product.
    - `rating` (float): Average rating of the product.
    - `stock` (int): Available stock of the product.
    - `brand` (str): Brand name of the product.
    - `thumbnail` (str): URL to the product's thumbnail image.
    - `images` (list[str]): List of URLs to the product's images.
    - `is_published` (bool): Indicates if the product is published.
    - `created_at` (datetime): Timestamp of product creation.
    - `category_id` (int): Foreign key referencing the Category model.
    
    Relationships:
    - `category`: Many-to-one relationship with the Category model.
    - `cart_items`: One-to-many relationship with the CartItem model.
    """
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    discount_percentage = Column(Float, nullable=False)
    rating = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    brand = Column(String, nullable=False)
    thumbnail = Column(String, nullable=False)
    images = Column(ARRAY(String), nullable=False)
    is_published = Column(Boolean, server_default="True", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"), nullable=False)

    # Relationships
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    category = relationship("Category", back_populates="products")
    cart_items = relationship("CartItem", back_populates="product")
