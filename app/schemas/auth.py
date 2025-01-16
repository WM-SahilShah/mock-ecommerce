"""
This module defines schemas for token-related responses used in authentication workflows.
"""

from app.config import CustomBaseModel
from fastapi import Form
from pydantic import Field

class TokenResponse(CustomBaseModel):
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
    token_type: str = Field("Bearer", description="Type of the token (default: Bearer).")
    expire_in: int = Field(..., description="Time in seconds before the access token expires.")


class CustomOAuth2PasswordRequestForm:
    """
    This class handles the OAuth2 password request form data. This form collects the user's username and password as part of the authentication process.

    Attributes:
    - `username` (str): The username of the user, provided as form data.
    - `password` (str): The unhashed password of the user, provided as form data.
    """
    def __init__(
        self,
        username: str = Form("{{username}}", description="The username of the user"),
        password: str = Form("{{password}}", description="The (unhashed) password of the user"),
    ) -> None:
        self.username = username
        self.password = password
