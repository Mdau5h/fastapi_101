from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from app.config import config

import uvicorn
import logging

from database.create import db_setup
from database.db_models import Base
from app.pydantic_models import NoteRequestModel
from database.ext.notes import get_note_by_id, create_note, get_all_notes, delete_note_by_id, update_note

from app.logger import init_logging

logger = logging.getLogger(__name__)

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     context = {'request': request}
#     return templates.TemplateResponse("index.html", context)
#
# @app.get("/api/v1/notes")
# async def get_notes():
#     return get_all_notes()
#
# @app.get("/api/v1/notes/{note_id}")
# async def get_note(note_id: int):
#     note_in_db = get_note_by_id(note_id)
#     if note_in_db:
#         return note_in_db
#     raise HTTPException(status_code=404, detail=f"Note with id == '{note_id}' does not exist!")
#
# @app.post("/api/v1/notes", status_code=201)
# async def post_note(note: NoteRequest):
#     note_in_db = create_note(
#         title=note.title,
#         content=note.content
#     )
#     if note_in_db:
#         return note_in_db
#
# @app.put("/api/v1/notes/{note_id}")
# async def put_note(note_id: int, note: NoteRequest):
#     note_in_db = get_note_by_id(note_id)
#     if note_in_db:
#         update_note(
#             id_=note_id,
#             title=note.title,
#             content=note.content
#         )
#         return get_note_by_id(note_id)
#     raise HTTPException(status_code=404, detail=f"Note with id == '{note_id}' does not exist!")
#
# @app.delete("/api/v1/notes/{note_id}", status_code=204)
# async def delete_note(note_id: int):
#     note_in_db = delete_note_by_id(note_id)
#     if note_in_db:
#         return {"id": note_in_db}
#     raise HTTPException(status_code=404, detail=f"Note with id == '{note_id}' does not exist!")

# @app.get("/js/{file_name}")
# async def return_js(file_name: str):
#     return FileResponse(f"js/{file_name}")

def main() -> None:
    init_logging()
    db_setup()
    logger.info('database is ready')
    # uvicorn.run("main:app", port=int(config.PORT), host=config.HOST, reload=True)

if __name__ == '__main__':
    main()
