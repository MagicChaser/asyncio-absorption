import asyncio

"""
asyncio.create_task(coro, *, name=None)
    将coro协程封装为一个Task对象并调度(安排其在事件循环中运行)，返回Task对象。
    name不为None，它将使用Task.set_name()来设为任务的名称
    该任务会在get_running_loop()返回的循环中执行，若当前线程没有在运行的循环则会抛出RuntimeError异常.
✅重要：保存一个指向此函数的结果的引用，以避免任务在执行过程中消失。事件循环将只保留对任务的弱引用。未在其他地方被引用的任务可能在任何时候被作为垃圾回收，即使是在他被完成之前。若需要可靠的"发射后不用管"后台任务，请将它们放到一个多项集中.
"""
background_tasks = set()

async def wait_func(n):
    print("AS")
    await asyncio.sleep(n)
    print("YNC")
    
    
async def main():
    for i in range(3):
        # 创建并立即运行，用于并发场景.
        task = asyncio.create_task(wait_func(i))    
        background_tasks.add(task)    
        
        # 为了防止永久保留对已完成任务的引用，让每个任务完成后从集合中移除自身的引用
        task.add_done_callback(background_tasks.discard)
        # 这个加入，以及移除操作，是必须的吗？有没有类似with方式开头的或其他方式的，自动加入、移除的？
    # 等待所有任务完成
    await asyncio.gather(*background_tasks)

asyncio.run(main())

    