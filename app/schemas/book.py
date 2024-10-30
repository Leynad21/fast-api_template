from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    description: str


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    description: str | None = None


class BookOut(BookBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
