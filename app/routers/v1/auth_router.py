# app/routers/v1/auth_router.py
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut, Token
from app.services.auth_service import register_user, authenticate_user
from app.core.config import settings
from app.db.session import get_db

router = APIRouter()


# Registration endpoint
@router.post("/signup", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Registers a new user.
    """
    new_user = register_user(db, user_data)
    return new_user


# Login endpoint
@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Authenticates a user and returns a JWT token.
    """
    access_token = authenticate_user(db, form_data.username, form_data.password)
    return {"access_token": access_token, "token_type": "bearer"}
