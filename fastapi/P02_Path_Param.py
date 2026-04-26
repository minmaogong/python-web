"""
    路径参数
"""

from  fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id):
    return {"user_id": user_id}

if __name__ == "__main__":
    # 直接在代码中启动uvicorn服务器
    uvicorn.run(
        "P02_Path_Param:app", # 指定要运行的FastAPI应用实例
        host="0.0.0.0", # 允许外部访问 （本地可通过127.0.0.1或localhost访问）
        port=8000, # 端口号
        reload=True, # 开发模式：代码修改后自动重启（生产环境去掉）
    )