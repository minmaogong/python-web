"""
    事件循环 以及协程的同步执行
"""
import asyncio
import time


# name: 任务名称
# delay: 睡眠时间 模拟一个IO操作，该操作执行需要delay秒
async def my_func(name, delay):
    print(f"任务{name}开始执行")
    # 模拟耗时操作
    await asyncio.sleep(delay)
    print(f"任务{name}执行结束")
    return  f"任务{name}的结果"

async def main_sync():
    print("串行执行：1s + 2s = 总耗时3s")
    await my_func("A", 1)
    await my_func("B", 2)

if __name__ == "__main__":
    #创建一个协程对象（顶级任务--执行的入口）      启动事件循环
    start_time = time.time()
    asyncio.run(main_sync())
    print(f"串行耗时：{time.time()-start_time:.2f}s")