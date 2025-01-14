from pydantic import BaseModel, Field

class TokenResponse(BaseModel):
    """Schema for token response."""
    access_token: str = Field(..., description="JWT access token for authentication")
    refresh_token: str = Field(..., description="JWT refresh token to obtain new access tokens")
    token_type: str = Field('Bearer', description="Type of the token (default: Bearer)")
    expire_in: int = Field(..., description="Time in seconds before the access token expires")
