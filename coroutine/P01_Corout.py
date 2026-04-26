"""
    协程对象的创建
"""
import asyncio

# 使用async定义的函数 就是协程函数
async def hello():
    print("Hello")
    # await 只能在协程函数内部使用
    await asyncio.sleep(1)
    print("World")

# 当调用协程函数的时候，函数不会立即执行， 返回的是一个协程对象
cor_obj = hello()
print(type(cor_obj))