import openpyxl
from schemas import TermCreate
from crud import create_term
from database import SessionLocal

def import_terms_from_xlsx(file_path: str):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    db = SessionLocal()
    for i, row in enumerate(sheet.iter_rows(min_row=2, values_only=True)):
        term = TermCreate(
            english=row[0],
            abbreviation=row[1],
            category=row[2],
            russian=row[3],
            turkmen=row[4],
            description_en=row[5],
            description_ru=row[6],
            description_tm=row[7],
        )
        create_term(db, term)
    db.close()
