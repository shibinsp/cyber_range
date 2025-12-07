from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db

router = APIRouter()

@router.get("/results")
async def get_scoring_results(db: AsyncSession = Depends(get_db)):
    """Get scoring results"""
    return []

@router.get("/leaderboard")
async def get_leaderboard(db: AsyncSession = Depends(get_db)):
    """Get leaderboard"""
    return []
