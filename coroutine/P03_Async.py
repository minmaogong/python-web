"""
    协程的异步调用执行
"""
import asyncio
import time


async def my_func(name, delay):
    print(f"任务{name}开始执行")
    await asyncio.sleep(delay)
    print(f"任务{name}执行结束")
    return f"结果 of {name}"

async def main_concurrent():
    print("--- 并发执行（总耗时 max(1s, 2s) = 2s）---")

    # 如果要并行执行 需要将协程对象封装为task，注册到事件循环上
    task1 = asyncio.create_task(my_func("C", 1))
    task2 = asyncio.create_task(my_func("D", 2))

    # 并发的执行任务， 并获取结果
    results = await asyncio.gather(task1, task2)

    print(f"所有的结果：{results}")

if __name__ == '__main__':
    start_time = time.time()
    # 启动事件循环，注册顶级任务
    asyncio.run(main_concurrent())
    print(f"并行耗时：{time.time() - start_time:.2f}s")