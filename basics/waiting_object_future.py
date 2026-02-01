import asyncio

"""
Futures:
    Future是一种特殊的低层级可等待对象，表示一个异步操作的最终结果。Future对象通常由事件循环或其他异步代码创建和使用。
    Future对象有助于协调不同任务之间的异步操作，允许一个任务等待另一个任务的结果。
    通常情况下，没有必要在应用层级的代码中创建Future对象.
    在asyncio中，Future对象通常不直接由用户创建，而是通过高级API（如asyncio.create_task()）间接创建。

async def main():
    await function_that_returns_a_future_object()

    # 也可以使用 asyncio.gather() 来等待多个 Future 对象
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_other_coroutine()
    )        
"""

