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

if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
