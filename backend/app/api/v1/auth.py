from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta
from app.core.config import settings
from app.db.session import get_db
from app.core import security
from pydantic import BaseModel, EmailStr

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

class Token(BaseModel):
    access_token: str
    token_type: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserRegister(BaseModel):
    email: EmailStr
    password: str
    role: str = "student"

@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    # TODO: Verify user credentials from database
    # This is a stub - implement actual user verification

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register")
async def register(user: UserRegister, db: AsyncSession = Depends(get_db)):
    """
    Register a new user
    """
    # TODO: Implement user registration logic
    # 1. Check if email already exists
    # 2. Hash password
    # 3. Create user in database
    # 4. Return success response

    return {"message": "User registered successfully", "email": user.email}

@router.post("/logout")
async def logout():
    """
    Logout user (client-side token removal)
    """
    return {"message": "Successfully logged out"}

@router.post("/refresh")
async def refresh_token(token: str = Depends(oauth2_scheme)):
    """
    Refresh access token
    """
    # TODO: Implement token refresh logic
    return {"access_token": "new_token", "token_type": "bearer"}
