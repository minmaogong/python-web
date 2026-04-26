"""
    第一个FastApi程序
"""
import uvicorn
from fastapi import FastAPI

# 创建web应用对象
app = FastAPI()

# 拦截客户端请求 将请求交给对应的方法进行处理
@app.get("/")
def root():
    return {"message": "welcome"}

@app.get("/student/{student_id}")
async def get_student(student_id: int):
    return {"student": f"{student_id}--王xx"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)