import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"Started at {time.strftime('%X')}")
    
    await say_after(1, 'Claude-')
    await say_after(2, "Code-")
    print(f"finished at {time.strftime('%X')}")

# asyncio.run(main())

"""
Started at 14:27:59
Claude-
Code-
finished at 14:28:02
"""