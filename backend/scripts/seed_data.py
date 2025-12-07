import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from app.core.config import settings
from app.core.security import get_password_hash
from app.db.base import Base
from app.models.role import Role
from app.models.user import User

async def seed_database():
    """Seed the database with initial data"""
    engine = create_async_engine(settings.DATABASE_URL, echo=True)

    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Create session
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        # Create roles
        roles_data = [
            {"name": "superadmin", "permissions": {"all": True}},
            {"name": "admin", "permissions": {"manage_users": True, "manage_scenarios": True}},
            {"name": "instructor", "permissions": {"create_scenarios": True, "manage_students": True}},
            {"name": "red", "permissions": {"run_attacks": True}},
            {"name": "blue", "permissions": {"defend": True, "view_logs": True}},
            {"name": "analyst", "permissions": {"view_reports": True}},
            {"name": "student", "permissions": {"participate": True}},
            {"name": "guest", "permissions": {"view_only": True}},
        ]

        for role_data in roles_data:
            role = Role(**role_data)
            session.add(role)

        await session.commit()

        # Get admin role
        result = await session.execute(select(Role.id).where(Role.name == "superadmin"))
        admin_role_id = result.scalar_one()

        # Create default admin user
        admin_user = User(
            email="admin@retrorange.local",
            hashed_password=get_password_hash("Admin123!"),
            role_id=admin_role_id,
        )
        session.add(admin_user)
        await session.commit()

        print("✅ Database seeded successfully!")
        print("📧 Admin credentials: admin@retrorange.local / Admin123!")

    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(seed_database())
