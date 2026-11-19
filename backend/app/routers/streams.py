from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.services.stream_service import StreamService
from app.schemas import LiveStreamCreate, LiveStreamUpdate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/streams", response_model=list[str])
def get_streams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stream_service = StreamService(db)
    streams = stream_service.get_streams(skip, limit)
    return [{"id": s.id, "channel_name": s.channel_name, "status": s.status, "bitrate_kbps": s.bitrate_kbps} for s in streams]

@router.post("/streams", status_code=status.HTTP_201_CREATED)
def create_stream(stream_data: LiveStreamCreate, db: Session = Depends(get_db)):
    stream_service = StreamService(db)
    # For now, assume user_id=1 (admin) or pass in header
    stream = stream_service.create_stream(stream_data, user_id=1)
    return {"id": stream.id, "channel_name": stream.channel_name}

@router.get("/streams/{stream_id}")
def get_stream(stream_id: int, db: Session = Depends(get_db)):
    stream_service = StreamService(db)
    stream = stream_service.get_stream(stream_id)
    if not stream:
        raise HTTPException(status_code=404, detail="Stream not found")
    return {"id": stream.id, "channel_name": stream.channel_name, "status": stream.status}

@router.put("/streams/{stream_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_stream(stream_id: int, stream_data: LiveStreamUpdate, db: Session = Depends(get_db)):
    stream_service = StreamService(db)
    stream_service.update_stream(stream_id, stream_data)
    return None

@router.delete("/streams/{stream_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_stream(stream_id: int, db: Session = Depends(get_db)):
    stream_service = StreamService(db)
    stream_service.delete_stream(stream_id)
    return None