from pydantic import BaseModel

class TermCreate(BaseModel):
    id: int | None = None  
    number: int  
    english: str
    russian: str | None = None
    turkmen: str | None = None
    abbreviation: str | None = None
    category: str | None = None
    description_en: str | None = None
    description_ru: str | None = None
    description_tm: str | None = None

    class Config:
        orm_mode = True
