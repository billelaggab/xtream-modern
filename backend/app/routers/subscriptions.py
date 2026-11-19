from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.services.subscription_service import SubscriptionService
from app.schemas import SubscriptionCreate, SubscriptionResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/subscriptions", response_model=list[SubscriptionResponse])
def get_subscriptions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    subscription_service = SubscriptionService(db)
    subscriptions = subscription_service.get_subscriptions(skip, limit)
    return subscriptions

@router.post("/subscriptions", status_code=status.HTTP_201_CREATED)
def create_subscription(subscription_data: SubscriptionCreate, db: Session = Depends(get_db)):
    subscription_service = SubscriptionService(db)
    subscription = subscription_service.create_subscription(subscription_data, user_id=1)
    return {"id": subscription.id, "status": subscription.status}

@router.get("/subscriptions/{subscription_id}")
def get_subscription(subscription_id: int, db: Session = Depends(get_db)):
    subscription_service = SubscriptionService(db)
    subscription = subscription_service.get_subscription(subscription_id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return {"id": subscription.id, "status": subscription.status}

@router.put("/subscriptions/{subscription_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_subscription(subscription_id: int, status: str, db: Session = Depends(get_db)):
    subscription_service = SubscriptionService(db)
    subscription = subscription_service.update_subscription(subscription_id, {"status": status})
    return None

@router.delete("/subscriptions/{subscription_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_subscription(subscription_id: int, db: Session = Depends(get_db)):
    subscription_service = SubscriptionService(db)
    subscription_service.delete_subscription(subscription_id)
    return None