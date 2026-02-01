import asyncio
from coroutines三种机制2 import say_after

"""
屏蔽取消操作
    awaitable asyncio.shield(aw)
    保护一个可等待对象，防止其被取消.
    若aw是一个协程，它将自动被作为任务调度.         
"""
async def main():
    task = asyncio.create_task(say_after(2, "Hi,Claude!🎉"))
    res = await asyncio.shield(task)    
    # line14相当于line11-12
    res = await say_after(2, "Hi,Claude!🎉")

"""
不同之处：若包含它的协程被取消，在say_after()中运行的任务不会被取消.从say_after()的角度看来，取消操作并没有发生.然而其调用者已被取消，因此await表达式然后会引发CancelledError.
若通过其他方式取消say_after()，e.g.:在其内部操作，则shield()也会取消.
如果希望完全忽略取消操作[不推荐]，则shield函数需要配合一个try、except代码段，如下：
"""
async def func():
    task = asyncio.create_task(say_after(3, "Beautiful Day!"))
    try:
        res = await asyncio.shield(task)
    except asyncio.CancelledError:
        res = None
"""
重要：保存一个传给此函数的任务的引用，以避免任务在执行过程中消失.事件循环将只保留对任务的弱引用.未在其他地方被引用的任务可能在任何时候被作为垃圾回收，即使是在他被完成之前.
"""    