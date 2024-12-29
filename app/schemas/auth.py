from app.schemas.users import UserBase, BaseConfig
from pydantic import BaseModel

class Signup(UserBase):
    "Schema for user signup details."
    id: None
    role: None
    is_active: None
    created_at: None
    carts: None

class UserOut(BaseModel):
    "Schema for user output with a message and user data."
    message: str
    data: UserBase

    class Config(BaseConfig):
        pass

class TokenResponse(BaseModel):
    "Schema for token response."
    access_token: str
    refresh_token: str
    token_type: str = 'Bearer'
    expires_in: int
