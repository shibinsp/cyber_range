from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db

router = APIRouter()

@router.get("/")
async def list_users(db: AsyncSession = Depends(get_db)):
    """List all users"""
    return []

@router.get("/{user_id}")
async def get_user(user_id: str, db: AsyncSession = Depends(get_db)):
    """Get user by ID"""
    return {"id": user_id}
