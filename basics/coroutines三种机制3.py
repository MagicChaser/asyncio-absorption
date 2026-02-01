import asyncio
import time
from coroutines三种机制2 import say_after

# create_task()函数用于并发运行，作为asyncio任务的多个协程.

async def main():
    task1 = asyncio.create_task(say_after(1, "White"))
    
    task2 = asyncio.create_task(say_after(2, 'Black'))    
    
    print(f"Started at {time.strftime('%X')}")
    
    # 等待直到两个任务都完成后（应该大概2s）
    await task1
    await task2
    
    print(f"finshed at {time.strftime('%X')}")
    
asyncio.run(main())

"""
Started at 14:44:05
White
Black
finshed at 14:44:07
"""
# 注意，预期的输出显示代码段的运行时间比之前快了 1 秒
