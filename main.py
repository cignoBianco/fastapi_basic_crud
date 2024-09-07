from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    text: str
    is_done: bool = False


items = []


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items


@app.get("/items")
def list_items(limit: int = 10):
    return items[0:limit]


@app.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item id {item_id} not found. ")


