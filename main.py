from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Simple Shop API")

class Item(BaseModel):
    id: int
    item: str

# インメモリストレージ
items = [
    Item(id=1, item="りんご"),
    Item(id=2, item="バナナ"),
    Item(id=3, item="オレンジ")
]

# 次のIDを管理するカウンター
next_id = 4

@app.get("/items", response_model=List[Item])
async def get_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    item = next((item for item in items if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", response_model=Item)
async def create_item(item_name: str):
    global next_id
    new_item = Item(id=next_id, item=item_name)
    items.append(new_item)
    next_id += 1
    return new_item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    item = next((item for item in items if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    items.remove(item)
    return {"message": f"Item {item_id} deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)