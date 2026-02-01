import asyncio


"""
超时
    coroutine asyncio.wait_for(aw, timeout)
    等待aw可等待对象完成，指定timeout描述后超时.
    若aw是一个协程，它将自动被作为任务调度.
    timeout可以为None，也可以为float或int型数值表示的等待秒数.若timeout为None，则等待直到完成.
    若发生超时，任务将取消并引发asyncio.TimeoutError.
    要避免任务取消，可加上shield()
    此函数将等待直到future确实被取消，所以总等待时间可能超过timeout.若再取消期间发生了异常，异常将会被传播.
    若等待被取消，则aw指定的对象也会被取消.    
"""
async def eternity():
    await asyncio.sleep(3600)
    print("123")

async def main():
    try:
        await asyncio.wait_for(eternity(), timeout=3.0)
    except asyncio.TimeoutError:
        print(f"报错：已超时...")  # 已超时，但e输出为什么是空？
    
asyncio.run(main())    