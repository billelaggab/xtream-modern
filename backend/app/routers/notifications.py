from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.services.notification_service import NotificationService
from app.schemas import NotificationCreate, NotificationResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/notifications", response_model=list[NotificationResponse])
def get_notifications(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notification_service = NotificationService(db)
    notifications = notification_service.get_notifications(user_id, skip, limit)
    return notifications

@router.post("/notifications", status_code=status.HTTP_201_CREATED)
def create_notification(notification_data: NotificationCreate, user_id: int, db: Session = Depends(get_db)):
    notification_service = NotificationService(db)
    notification = notification_service.create_notification(notification_data, user_id)
    return notification

@router.put("/notifications/{notification_id}", status_code=status.HTTP_204_NO_CONTENT)
def mark_as_read(notification_id: int, db: Session = Depends(get_db)):
    notification_service = NotificationService(db)
    notification_service.mark_as_read(notification_id)
    return None

@router.delete("/notifications/{notification_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_notification(notification_id: int, db: Session = Depends(get_db)):
    notification_service = NotificationService(db)
    notification_service.delete_notification(notification_id)
    return None