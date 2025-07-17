from sqlalchemy.orm import Session
from sqlalchemy import select, distinct
from models import Term
from schemas import TermCreate

def create_term(db: Session, term: TermCreate):
    db_term = Term(**term.dict())
    db.add(db_term)
    db.commit()
    db.refresh(db_term)
    return db_term

def get_terms(db: Session, categories: list[str] = None, skip: int = 0, limit: int = 30):
    query = db.query(Term)
    if categories:
        query = query.filter(Term.category.in_(categories))
    return query.offset(skip).limit(limit).all()



def get_all_categories(db: Session):
    result = db.query(distinct(Term.category)).order_by(Term.category).all()
    return [row[0] for row in result if row[0]]  
