from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "World"}


@app.get("/{item_id}")
def home(item_id: int):
    return {"item_id": item_id}


