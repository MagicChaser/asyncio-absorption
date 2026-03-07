import asyncio 
import itertools


async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        try:
            await asyncio.sleep(1)        
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')    

async def slow() -> int:
    await asyncio.sleep(5)
    return 36
    
async def supervisor() -> int:
    spinner = asyncio.create_task(spin('THINKING...'))
    print(f"spinner object:{spinner}")
    res = await slow()
    spinner.cancel()
    return res

def main():
    res = asyncio.run(supervisor())
    print(f"Answer: {res}")
    
if "__main__" == __name__:
    main()
    