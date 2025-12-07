from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import all models here for Alembic
from app.models.role import Role  # noqa
from app.models.user import User  # noqa
from app.models.scenario import Scenario  # noqa
from app.models.virtual_machine import VirtualMachine  # noqa
