from typing import Optional, List
from sqlalchemy.orm import Session
from app.models import LiveStream
from app.schemas import LiveStreamCreate, LiveStreamUpdate

class StreamService:
    def __init__(self, db: Session):
        self.db = db

    def get_streams(self, skip: int = 0, limit: int = 100) -> List[LiveStream]:
        return self.db.query(LiveStream).offset(skip).limit(limit).all()

    def get_stream(self, stream_id: int) -> Optional[LiveStream]:
        return self.db.query(LiveStream).filter(LiveStream.id == stream_id).first()

    def get_streams_by_user(self, user_id: int) -> List[LiveStream]:
        return self.db.query(LiveStream).filter(LiveStream.user_id == user_id).all()

    def create_stream(self, stream_data: LiveStreamCreate, user_id: int) -> LiveStream:
        stream = LiveStream(
            user_id=user_id,
            channel_name=stream_data.channel_name,
            bitrate_kbps=stream_data.bitrate_kbps,
        )
        self.db.add(stream)
        self.db.commit()
        self.db.refresh(stream)
        return stream

    def update_stream(self, stream_id: int, stream_data: LiveStreamUpdate) -> Optional[LiveStream]:
        stream = self.get_stream(stream_id)
        if not stream:
            return None
        for key, value in stream_data.dict(exclude_unset=True).items():
            setattr(stream, key, value)
        self.db.commit()
        self.db.refresh(stream)
        return stream

    def delete_stream(self, stream_id: int) -> bool:
        stream = self.get_stream(stream_id)
        if not stream:
            return False
        self.db.delete(stream)
        self.db.commit()
        return True