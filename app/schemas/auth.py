from pydantic import BaseModel

class TokenResponse(BaseModel):
    "Schema for token response."
    access_token: str
    refresh_token: str
    token_type: str = 'Bearer'
    expires_in: int
