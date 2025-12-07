from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db

router = APIRouter()

@router.get("/")
async def list_vms(db: AsyncSession = Depends(get_db)):
    """List all virtual machines"""
    return []

@router.post("/{vm_id}/start")
async def start_vm(vm_id: str):
    """Start a VM"""
    return {"message": "VM started", "vm_id": vm_id}

@router.post("/{vm_id}/stop")
async def stop_vm(vm_id: str):
    """Stop a VM"""
    return {"message": "VM stopped", "vm_id": vm_id}
