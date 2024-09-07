from fastapi import FastAPI, status, HTTPException

app = FastAPI()

items = []


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items


@app.get("/items")
def get_item():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item id {item_id} not found. ")


