import asyncio
import datetime, time

"""
coroutine asyncio.sleep(delay, result=None)
    阻塞delay指定的秒数。
    若指定了result，则当协程完成时将其返回给调用者.
    sleep()总是会挂起当前任务，以允许其他任务执行.
    将delay设为0将提供一个经优化的路径以允许其他任务运行.这可供长期间运行的函数使用以避免在函数调用的全过程中阻塞事件循环.
Deprecated since version 3.8, removed in version 3.10: loop 形参。 这个函数从 3.7 开始就会隐式地获取当前正在运行的事件循环。    
"""

async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        # 事件循环继续运行，其他任务可执行，仅暂停当前任务(异步)
        await asyncio.sleep(1)
        # 事件循环被冻结，其他任务无法运行，阻塞整个线程(同步).
        time.sleep(1)
        

asyncio.run(display_date())

"""
2026-01-06 14:11:30.692952
2026-01-06 14:11:31.693787
2026-01-06 14:11:32.695130
2026-01-06 14:11:33.697547
2026-01-06 14:11:34.699563
"""    