import asyncio


"""
asyncio.run(coro, *, debug=False)
    执行coroutine coro并返回结果。
✅此函数会运行传入的协程，负责管理asyncio事件循环，终结异步生成器，并关闭线程池.
✅当有其他asyncio事件循环正在运行时，调用此函数会抛出一个RuntimeError异常.
✅若debug为True，事件循环将以调试模式运行.
✅此函数总是会创建一个新的事件循环并在结束时关闭它。它应当被用作asyncio程序的主入口点，理想情况下只调用一次.     
"""

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(main())    