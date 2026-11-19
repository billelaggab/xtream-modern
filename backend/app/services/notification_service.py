from typing import Optional, List
from sqlalchemy.orm import Session
from app.models import Notification
from app.schemas import NotificationCreate

class NotificationService:
    def __init__(self, db: Session):
        self.db = db

    def get_notifications(self, user_id: int, skip: int = 0, limit: int = 100) -> List[Notification]:
        return self.db.query(Notification).filter(Notification.user_id == user_id).offset(skip).limit(limit).all()

    def get_notification(self, notification_id: int) -> Optional[Notification]:
        return self.db.query(Notification).filter(Notification.id == notification_id).first()

    def create_notification(self, notification_data: NotificationCreate, user_id: int) -> Notification:
        notification = Notification(
            user_id=user_id,
            message=notification_data.message,
        )
        self.db.add(notification)
        self.db.commit()
        self.db.refresh(notification)
        return notification

    def mark_as_read(self, notification_id: int) -> Optional[Notification]:
        notification = self.get_notification(notification_id)
        if not notification:
            return None
        notification.read = True
        self.db.commit()
        self.db.refresh(notification)
        return notification

    def delete_notification(self, notification_id: int) -> bool:
        notification = self.get_notification(notification_id)
        if not notification:
            return False
        self.db.delete(notification)
        self.db.commit()
        return True