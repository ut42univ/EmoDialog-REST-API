from . import schemas, models
from .crud import DiaryCRUD
from .database import SessionLocal, engine
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def Hello():
    return {"Hello":"World!"}


@app.get("/diaries/", response_model=List[schemas.Diary])
async def read_diaries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    diary_crud = DiaryCRUD(db=db, model=models.Diary)
    diaries = diary_crud.get_diaries(skip=skip, limit=limit)

    return diaries


@app.get("/diaries/{diary_id}", response_model=schemas.Diary)
async def read_diary(diary_id: int, db: Session = Depends(get_db)):
    diary_crud = DiaryCRUD(db=db, model=models.Diary)
    db_diary = diary_crud.get_diary(diary_id=diary_id)

    if db_diary is None:
        raise HTTPException(status_code=404, detail="Diary not found")

    return db_diary


@app.post("/diaries/", response_model=schemas.Diary)
async def create_diary(diary: schemas.DiaryCreate, db: Session = Depends(get_db)):
    diary_crud = DiaryCRUD(db=db, model=models.Diary)

    return diary_crud.create_diary(diary=diary)


@app.put("/diaries/{diary_id}", response_model=schemas.Diary)
async def update_diary(diary_id: int, diary: schemas.DiaryCreate, db: Session = Depends(get_db)):
    diary_crud = DiaryCRUD(db=db, model=models.Diary)

    return diary_crud.update_diary(diary_id=diary_id, diary=diary)


@app.delete("/diaries/{diary_id}", response_model=schemas.Diary)
async def delete_diary(diary_id: int, db: Session = Depends(get_db)):
    diary_crud = DiaryCRUD(db=db, model=models.Diary)

    return diary_crud.delete_diary(diary_id=diary_id)
