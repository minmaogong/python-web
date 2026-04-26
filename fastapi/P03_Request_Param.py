"""
    请求参数
"""

from fastapi import FastAPI
import uvicorn

app = FastAPI()

items_list = [{"item1": "Foo"}, {"item2": "Bar"}, {"item3": "Baz"}]

@app.get("/items/")
async def read_items(start: int = 0, limit: int = 10):
    return items_list[start : start + limit]

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

if __name__ == "__main__":
    uvicorn.run(
        "P03_Request_Param:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )