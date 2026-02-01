import asyncio
"""
并发运行任务
    awaitable asyncio.gather(*aws, return_exceptions=False)
    并发运行aws序列中的可等待对象. 
    若aws中的某个可等待对象为协程，它将自动被作为一个任务调度.
    若所有可等待对象都成功完成，结果将是一个由所有返回值聚合而成的列表.结果值的顺序于aws中的可等待对象的顺序一致.
    若return_exceptions为False(默认),所引发的首个异常会立即传播给等待gather()的任务.aws序列中的其他可等待对象不会被取消并继续运行; 若为True,异常会和成功的结果一样处理，并聚合到结果列表.
    若gather()被取消，所有被提交(尚未完成)的可等待对象也会被取消.
    若aws序列中的任一Task或Future对象被取消，它将被当作引发了CancelledError一样处理--在此情况下gather()调用不会被取消.这是为了防止一个已提交的Task/Future被取消导致其他Tasks/Future也被取消.
"""
# 这是属于单线程中的多协程运行
async def factorial(name, n) -> int:
    f = 1
    for i in range(2, n + 1):
        print(f"Task-{name}: Compute factorial({n}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task-{name}: factorial({n}) = {f}")    
    return f

async def main():
    # 调度3个并发函数    如果有多个呢？有别的写法吗？
    L = await asyncio.gather(
        factorial("A", 3),
        factorial("B", 5),
        factorial("C", 7)
    )
    print(L)
    
asyncio.run(main())

"""
Task-A: Compute factorial(3), currently i=2...
Task-B: Compute factorial(5), currently i=2...
Task-C: Compute factorial(7), currently i=2...
Task-A: Compute factorial(3), currently i=3...
Task-B: Compute factorial(5), currently i=3...
Task-C: Compute factorial(7), currently i=3...
Task-A: factorial(3) = 6
Task-B: Compute factorial(5), currently i=4...
Task-C: Compute factorial(7), currently i=4...
Task-B: Compute factorial(5), currently i=5...
Task-C: Compute factorial(7), currently i=5...
Task-B: factorial(5) = 120
Task-C: Compute factorial(7), currently i=6...
Task-C: Compute factorial(7), currently i=7...
Task-C: factorial(7) = 5040
[6, 120, 5040]

分析：若return_exceptions为False，即在gather()被标记为已完成后取消它将不会取消任何已提交的可等待对象.e.g.:在将一个一场传播给调用者之后，gather可被标记为已完成，因此，在从gather获取一个(由可等待对象所引发的)异常之后调用gather.cancel()将不会取消任何其他可等待对象.
"""
