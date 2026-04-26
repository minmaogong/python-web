"""
    请求体传参
"""

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

# 定义数据模型类，需要继承BaseModel的类
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

app = FastAPI()

@app.post("/items/")
async  def create_item(item: Item):
    return item

if __name__ == "__main__":
    uvicorn.run(
        "P04_Post:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )