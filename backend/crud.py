from sqlalchemy.orm import Session
from . import models, schemas


class CRUDBase:
    def __init__(self, db: Session):
        self.db = db


class DiaryCRUD(CRUDBase):
    def __init__(self, db: Session, model: models.Diary):
        super().__init__(db)
        self.model = model
    
    def get_diary(self, diary_id: int):
        return self.db.query(self.model).filter(self.model.id == diary_id).first()
    
    def get_diaries(self, skip: int = 0, limit: int = 100):
        return self.db.query(self.model).offset(skip).limit(limit).all()
    
    def create_diary(self, diary: schemas.DiaryCreate):
        db_diary = self.model(title=diary.title, body=diary.body)
        self.db.add(db_diary)
        self.db.commit()
        self.db.refresh(db_diary)
        return db_diary
    
    def update_diary(self, diary_id: int, diary: schemas.DiaryCreate):
        db_diary = self.db.query(self.model).filter(self.model.id == diary_id).first()
        db_diary.title = diary.title
        db_diary.body = diary.body
        self.db.commit()
        self.db.refresh(db_diary)
        return db_diary
    
    def delete_diary(self, diary_id: int):
        db_diary = self.db.query(self.model).filter(self.model.id == diary_id).first()
        self.db.delete(db_diary)
        self.db.commit()
        return db_diary
