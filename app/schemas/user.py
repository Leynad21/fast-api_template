# app/schemas/user.py
from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    """Schema for creating a new user (e.g., during signup)."""

    username: str
    password: str


class UserOut(BaseModel):
    """Schema for returning user data in responses."""

    id: int
    username: str

    class Config:
        orm_mode = True  # Enable ORM mode for compatibility with SQLAlchemy models


class Token(BaseModel):
    """Schema for the token returned during login."""

    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Schema for the data extracted from a JWT token."""

    username: Optional[str] = None
