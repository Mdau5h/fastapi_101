from pydantic import BaseModel, Field

class Note(BaseModel):
    id: int
    title: str = Field(..., max_length=50)
    content: str = Field(...)

class NoteRequest(BaseModel):
    title: str = Field(..., max_length=50)
    content: str = Field(...)