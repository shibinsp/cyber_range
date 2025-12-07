from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import JSONB
from app.db.base import Base

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    permissions = Column(JSONB, default={})
