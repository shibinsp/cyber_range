from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB, INET, MACADDR
from sqlalchemy.sql import func
from app.db.base import Base
import uuid

class VirtualMachine(Base):
    __tablename__ = "virtual_machines"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    type = Column(String)
    ip = Column(INET)
    mac = Column(MACADDR)
    status = Column(String, default="stopped")
    last_seen = Column(DateTime(timezone=True))
    snapshot_id = Column(String)
    vm_metadata = Column(JSONB, default={})
