import itertools
import time
from threading import Thread, Event


def spin(msg: str, done: Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(0.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='', flush=True)

def slow() -> int:
    time.sleep(5)        
    return 42