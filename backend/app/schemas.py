from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class UserCreate(BaseModel):
    username: str = Field(..., max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None

class UserResponse(UserCreate):
    id: int
    created_at: datetime
    updated_at: datetime | None = None
    is_active: bool = True
    role: str

class LiveStreamCreate(BaseModel):
    channel_name: str = Field(..., max_length=255)
    bitrate_kbps: int = 1280

class LiveStreamUpdate(BaseModel):
    status: str = "live"  # live, paused, completed, deleted

class VODCreate(BaseModel):
    title: str = Field(..., max_length=255)
    description: str | None = None
    duration_minutes: int = Field(..., gt=0)
    file_path: str = Field(..., max_length=500)

class VODUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    duration_minutes: Optional[int] = None
    file_path: Optional[str] = None

class CategoryCreate(BaseModel):
    name: str = Field(..., max_length=100)
    parent_category_id: Optional[int] = None

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    parent_category_id: Optional[int] = None

class SubscriptionCreate(BaseModel):
    channel_id: int

class SubscriptionUpdate(BaseModel):
    status: str = "active"

class NotificationCreate(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000)