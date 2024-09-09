from sqlalchemy.orm import Session
import models
import schemas


def get_diary(db: Session, diary_id: int):
    return db.query(models.Diary).filter(models.Diary.id == diary_id).first()


def get_diaries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Diary).offset(skip).limit(limit).all()


def create_diary(db: Session, diary: schemas.DiaryCreate):
    db_diary = models.Diary(title=diary.title, body=diary.body)
    db.add(db_diary)
    db.commit()
    db.refresh(db_diary)
    return db_diary


def update_diary(db: Session, diary_id: int, diary: schemas.DiaryCreate):
    db_diary = db.query(models.Diary).filter(models.Diary.id == diary_id).first()
    db_diary.title = diary.title
    db_diary.body = diary.body
    db.commit()
    db.refresh(db_diary)
    return db_diary


def delete_diary(db: Session, diary_id: int):
    db_diary = db.query(models.Diary).filter(models.Diary.id == diary_id).first()
    db.delete(db_diary)
    db.commit()
    return db_diary