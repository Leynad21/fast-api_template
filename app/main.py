# app/main.py
from fastapi import FastAPI
from app.core.config import settings
from app.routers.v1 import auth_router, books_router
from app.db.session import engine, Base

app = FastAPI(title=settings.app_name)

app.include_router(auth_router.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(books_router.router, prefix="/api/v1/books", tags=["books"])

# Uncomment to automatically create tables (for development only)
Base.metadata.create_all(bind=engine)
