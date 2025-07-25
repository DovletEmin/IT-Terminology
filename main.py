from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas
from crud import get_terms, get_all_categories

from typing import Annotated

# обёртка над sync функцией
import asyncio

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Term Dictionary API",
    version="1.0.0",   
)

origins = [
    "*"                            
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,         
    allow_credentials=True,
    allow_methods=["*"],           
    allow_headers=["*"],          
)

# ---------------------------------------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/terms", response_model=list[schemas.TermCreate])
async def read_terms(
    category: Annotated[list[str] | None, Query()] = None,
    skip: int = 0,
    limit: int = 1870,
    db: Session = Depends(get_db)
):
    terms = await get_terms_async(db, category, skip, limit)
    return [
        schemas.TermCreate(number=skip + i + 1, **term.__dict__)
        for i, term in enumerate(terms)
    ]


async def get_terms_async(db: Session, category: list[str] | None, skip: int = 0, limit: int = 1870):
    return await asyncio.to_thread(get_terms, db, category, skip, limit)

@app.get("/categories", response_model=list[str])
async def read_categories(db: Session = Depends(get_db)):
    return await asyncio.to_thread(get_all_categories, db)



# from import_xlsx import import_terms_from_xlsx
# import_terms_from_xlsx("excel_sorted.xlsx")
 