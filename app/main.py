# /app/main.py
from fastapi import FastAPI
from app.api.api import api_router
from app.db.base import Base
from app.db.session import engine

# This command creates all tables in the database based on the models
# It should ideally be handled by a migration tool like Alembic in production
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Project with JWT and SQLAlchemy",
    description="A starter project for FastAPI with MySQL and JWT authentication.",
    version="0.1.0",
)

app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}