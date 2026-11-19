from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.services.auth_service import AuthService
from app.schemas import UserCreate, UserResponse
from app.core.security import oauth2_scheme
from app.core.exceptions import AuthException, NotFoundException

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/auth/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    existing_user = auth_service.get_user_by_username(user_data.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    return auth_service.create_user(user_data)

@router.post("/auth/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    user = auth_service.authenticate_user(username, password)
    if not user:
        raise AuthException("Incorrect username or password")
    return {"username": user.username, "user_id": user.id, "is_active": user.is_active}