from pydantic import BaseModel, Field

class NoteModel(BaseModel):
    id: int
    title: str = Field(..., max_length=50)
    content: str = Field(...)

class NoteRequestModel(BaseModel):
    title: str = Field(..., max_length=50)
    content: str = Field(...)
