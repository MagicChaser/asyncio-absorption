import asyncio

async def main():
    print("Hello Async Func.")
    await asyncio.sleep(3)
    print("Hi! Claude!~")


if __name__ == "__main__":
    asyncio.run(main())  
    
    
"""
(data_pipeline) blackcat@Admin:~/asyncio-absorption$ python -m basics.coroutines
Hello Async Func.
Hi! Claude!~
"""