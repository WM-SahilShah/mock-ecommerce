"""
App > Config
==========
This module contains the system-wide configuration components for the application, including logging, 
response handling, security, and settings.

Modules:
- logging: Setup and configuration for application logging.
- responses: Utilities for standardized API responses and HTTP exceptions.
- security: Authentication and authorization utilities.
- settings: Application and environment configurations.
"""

from .logging import logger
from .responses import CustomBaseModel, ResponseHandler
from .security import auth_scheme, get_password_hash, verify_password, get_user_token, get_token_payload, get_current_user, check_admin_role
from .settings import DB_URL, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY

__all__ = [
    "logger",    
    "CustomBaseModel", "ResponseHandler",
    "auth_scheme","get_password_hash", "verify_password", "get_user_token", "get_token_payload", "get_current_user", "check_admin_role",
    "DB_URL", "ACCESS_TOKEN_EXPIRE_MINUTES", "ALGORITHM", "SECRET_KEY"
]
