from pydantic import BaseModel
from datetime import datetime


class DiaryBase(BaseModel):
    title: str
    body: str


class DiaryCreate(DiaryBase):
    pass


class Diary(DiaryBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
