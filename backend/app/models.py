from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class User(BaseModel):
    id: int
    username: str
    email: str
    password_hash: str
    created_at: datetime
    updated_at: datetime = None
    is_active: bool = True
    role: str = "user"

class LiveStream(BaseModel):
    id: int
    user_id: int
    channel_name: str
    status: str
    start_time: datetime
    end_time: datetime | None = None
    bitrate_kbps: int = 1280

class VOD(BaseModel):
    id: int
    user_id: int
    title: str
    description: str | None = None
    duration_minutes: int
    file_path: str
    created_at: datetime = None

class Category(BaseModel):
    id: int
    name: str
    parent_category_id: int | None = None
    path: str

class Subscription(BaseModel):
    id: int
    user_id: int
    channel_id: int
    started_at: datetime
    ended_at: datetime | None = None
    status: str = "active"

class Notification(BaseModel):
    id: int
    user_id: int
    message: str
    read: bool = False
    created_at: datetime = None