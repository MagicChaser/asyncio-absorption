import asyncio

"""
可等待对象：
    若一个对象可以在await表达式中使用，则称该对象为可等待对象（awaitable object）。许多asyncio API都被设计为接受可等待对象。
    可等待对象有三种主要类型：
        协程（coroutine）：由async def定义的函数返回的对象。
        任务（Task）：由asyncio.create_task()或asyncio.ensure_future()创建的对象，用于调度协程的执行。
        期物（Future）：表示一个异步操作的最终结果的对象，通常由事件循环或其他异步代码创建和使用。
"""

async def nested():
    return 42

async def main():
    # 若我们仅调用nested(), 什么都不会发生. 会创建一个协程对象，但不会等待它，所以它根本不会运行.
    # nested()
    
    # 换个方式等待它
    print(await nested())

asyncio.run(main())    