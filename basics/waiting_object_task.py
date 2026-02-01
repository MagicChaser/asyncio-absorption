import asyncio


"""
任务：被用来“并行的”调度协程
当一个协程通过asyncio.create_task()等函数  封装为一个任务，此协程会被自动调度执行。
"""

async def nested():
    return 42

async def main():
    # 安排nested()很快同时运行带有main
    task = asyncio.create_task(nested())
    
    # “task”现在可用于取消“nested()”，或者也可以直接等待，直至其完成：
    await task

asyncio.run(main())