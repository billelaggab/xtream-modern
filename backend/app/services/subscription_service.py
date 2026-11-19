from typing import Optional, List
from sqlalchemy.orm import Session
from app.models import Subscription
from app.schemas import SubscriptionCreate, SubscriptionUpdate

class SubscriptionService:
    def __init__(self, db: Session):
        self.db = db

    def get_subscriptions(self, skip: int = 0, limit: int = 100) -> List[Subscription]:
        return self.db.query(Subscription).offset(skip).limit(limit).all()

    def get_subscription(self, subscription_id: int) -> Optional[Subscription]:
        return self.db.query(Subscription).filter(Subscription.id == subscription_id).first()

    def get_subscriptions_by_user(self, user_id: int) -> List[Subscription]:
        return self.db.query(Subscription).filter(Subscription.user_id == user_id).all()

    def create_subscription(self, subscription_data: SubscriptionCreate, user_id: int) -> Subscription:
        subscription = Subscription(
            user_id=user_id,
            channel_id=subscription_data.channel_id,
        )
        self.db.add(subscription)
        self.db.commit()
        self.db.refresh(subscription)
        return subscription

    def update_subscription(self, subscription_id: int, subscription_data: SubscriptionUpdate) -> Optional[Subscription]:
        subscription = self.get_subscription(subscription_id)
        if not subscription:
            return None
        for key, value in subscription_data.dict(exclude_unset=True).items():
            setattr(subscription, key, value)
        self.db.commit()
        self.db.refresh(subscription)
        return subscription

    def cancel_subscription(self, subscription_id: int) -> Optional[Subscription]:
        return self.update_subscription(subscription_id, SubscriptionUpdate(status="cancelled"))

    def delete_subscription(self, subscription_id: int) -> bool:
        subscription = self.get_subscription(subscription_id)
        if not subscription:
            return False
        self.db.delete(subscription)
        self.db.commit()
        return True