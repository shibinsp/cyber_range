from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db

router = APIRouter()

@router.get("/")
async def get_topology(db: AsyncSession = Depends(get_db)):
    """Get network topology"""
    return {"nodes": [], "edges": []}
