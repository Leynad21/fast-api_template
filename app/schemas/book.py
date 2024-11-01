from pydantic import BaseModel, Field, validator

class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Title of the book.")
    author: str = Field(..., min_length=1, max_length=50, description="Author of the book.")
    description: str = Field(..., min_length=10, max_length=500, description="Brief description of the book.")

    @validator("title")
    def title_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("Title cannot be empty or whitespace.")
        return value

    @validator("author")
    def author_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("Author cannot be empty or whitespace.")
        return value


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
