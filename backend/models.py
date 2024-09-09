from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
import pytz


class Diary(Base):
    __tablename__ = "diaries"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    created_at = Column(String, default=datetime.now(pytz.timezone('Asia/Tokyo')))
    updated_at = Column(String, default=datetime.now(pytz.timezone('Asia/Tokyo')), onupdate=datetime.now(pytz.timezone('Asia/Tokyo')))
