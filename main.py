from fastapi import FastAPI, HTTPException
from typing import List
import uvicorn
from database.models import Note

db:List[Note] = [
    Note(
        id=0,
        title="aaa",
        content="bbb"
    ),
    Note(
        id=1,
        title="ccc",
        content="ddd"
    )
]

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello, world!"}

@app.get("/api/v1/notes")
async def get_notes():
    return db

@app.post("/api/v1/notes", status_code=201)
async def create_note(note: Note):
    db.append(note)
    return note

@app.delete("/api/v1/notes/{note_id}", status_code=204)
async def delete_note(note_id: int):
    for note in db:
        if note.id == note_id:
            db.remove(note)
            return
    raise HTTPException(status_code=404, detail=f"Note with id == '{note_id}' does not exist!")

if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
