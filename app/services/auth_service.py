from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.crud.user_crud import create_user, get_user_by_username
from app.core.security import verify_password, create_access_token
from fastapi import HTTPException, status
from datetime import timedelta
from app.core.config import settings


def register_user(db: Session, user_data: UserCreate):
    db_user = get_user_by_username(db, user_data.username)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    return create_user(db, user_data)


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    return create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
