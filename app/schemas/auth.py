"""
This module defines schemas for token-related responses used in authentication workflows.
"""

from pydantic import BaseModel, Field

class TokenResponse(BaseModel):
    """
    Represents the schema for a token response.

    Attributes:
    - `access_token` (str): JWT access token for authentication.
    - `refresh_token` (str): JWT refresh token to obtain new access tokens.
    - `token_type` (str): Type of the token (`Bearer`).
    - `expire_in` (int): Time in seconds before the access token expires.
    """
    access_token: str = Field(..., description="JWT access token for authentication.")
    refresh_token: str = Field(..., description="JWT refresh token to obtain new access tokens.")
    token_type: str = Field('Bearer', description="Type of the token (default: Bearer).")
    expire_in: int = Field(..., description="Time in seconds before the access token expires.")
