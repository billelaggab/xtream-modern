from typing import Optional, List
from sqlalchemy.orm import Session
from app.models import VOD, Category
from app.schemas import VODCreate, VODUpdate, CategoryCreate, CategoryUpdate

class MediaService:
    def __init__(self, db: Session):
        self.db = db

    def get_vods(self, skip: int = 0, limit: int = 100) -> List[VOD]:
        return self.db.query(VOD).offset(skip).limit(limit).all()

    def get_vod(self, vod_id: int) -> Optional[VOD]:
        return self.db.query(VOD).filter(VOD.id == vod_id).first()

    def get_vods_by_user(self, user_id: int) -> List[VOD]:
        return self.db.query(VOD).filter(VOD.user_id == user_id).all()

    def create_vod(self, vod_data: VODCreate, user_id: int) -> VOD:
        vod = VOD(
            user_id=user_id,
            title=vod_data.title,
            description=vod_data.description,
            duration_minutes=vod_data.duration_minutes,
            file_path=vod_data.file_path,
        )
        self.db.add(vod)
        self.db.commit()
        self.db.refresh(vod)
        return vod

    def update_vod(self, vod_id: int, vod_data: VODUpdate) -> Optional[VOD]:
        vod = self.get_vod(vod_id)
        if not vod:
            return None
        for key, value in vod_data.dict(exclude_unset=True).items():
            setattr(vod, key, value)
        self.db.commit()
        self.db.refresh(vod)
        return vod

    def delete_vod(self, vod_id: int) -> bool:
        vod = self.get_vod(vod_id)
        if not vod:
            return False
        self.db.delete(vod)
        self.db.commit()
        return True

    def get_categories(self, skip: int = 0, limit: int = 100) -> List[Category]:
        return self.db.query(Category).offset(skip).limit(limit).all()

    def get_category(self, category_id: int) -> Optional[Category]:
        return self.db.query(Category).filter(Category.id == category_id).first()

    def create_category(self, category_data: CategoryCreate) -> Category:
        category = Category(
            name=category_data.name,
            parent_category_id=category_data.parent_category_id,
            path=f"/{category_data.name}",
        )
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category

    def update_category(self, category_id: int, category_data: CategoryUpdate) -> Optional[Category]:
        category = self.get_category(category_id)
        if not category:
            return None
        for key, value in category_data.dict(exclude_unset=True).items():
            setattr(category, key, value)
        self.db.commit()
        self.db.refresh(category)
        return category

    def delete_category(self, category_id: int) -> bool:
        category = self.get_category(category_id)
        if not category:
            return False
        self.db.delete(category)
        self.db.commit()
        return True