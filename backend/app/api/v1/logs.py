from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db

router = APIRouter()

@router.get("/search")
async def search_logs(q: str = "", db: AsyncSession = Depends(get_db)):
    """Search logs in Elasticsearch"""
    return {"results": [], "total": 0}
