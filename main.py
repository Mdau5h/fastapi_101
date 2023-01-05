from fastapi import FastAPI, HTTPException
import uvicorn
import logging

from database.create import rollout as init_db
from database.models import NoteRequest
from database.ext.notes import get_note_by_id, create_note, get_all_notes, delete_note_by_id, update_note

from app.logger import init_logging

logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello, world!"}

@app.get("/api/v1/notes")
async def get_notes():
    return get_all_notes()

@app.get("/api/v1/notes/{note_id}")
async def get_note(note_id: int):
    note_in_db = get_note_by_id(note_id)
    if note_in_db:
        return note_in_db
    raise HTTPException(status_code=404, detail=f"Note with id == '{note_id}' does not exist!")


@app.post("/api/v1/notes", status_code=201)
async def post_note(note: NoteRequest):
    create_note(
        title=note.title,
        content=note.content
    )
    # todo: return note_id
    return note

@app.put("/api/v1/notes/{note_id}")
async def put_note(note_id: int, note: NoteRequest):
    note_in_db = get_note_by_id(note_id)
    if note_in_db:
        update_note(
            id_=note_id,
            title=note.title,
            content=note.content
        )
        return
    raise HTTPException(status_code=404, detail=f"Note with id == '{note_id}' does not exist!")

@app.delete("/api/v1/notes/{note_id}", status_code=204)
async def delete_note(note_id: int):
    note_in_db = get_note_by_id(note_id)
    if note_in_db:
        delete_note_by_id(note_id)
        return
    raise HTTPException(status_code=404, detail=f"Note with id == '{note_id}' does not exist!")

def main() -> None:
    init_logging()
    init_db()
    logger.info('database is ready')
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)

if __name__ == '__main__':
    main()
