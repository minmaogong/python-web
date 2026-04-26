from fastapi import FastAPI
from routers import user, item
import uvicorn

app = FastAPI(title="路由分发示例")

# 挂载用户路由：所有 /users 开头的请求由 user.router 处理
app.include_router(user.router)

# 挂载商品路由：所有 /items 开头的 请求由 item.router 处理
app.include_router(item.router)

# 主应用自身也可以定义路由
@app.get("/")
def root():
    return {"message": "欢迎访问主页"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )

