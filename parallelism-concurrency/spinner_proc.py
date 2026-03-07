import itertools
import time
from multiprocessing import Process, Event
from multiprocessing import synchronize

# 进程实现旋转指针
def spin(msg: str, done: synchronize.Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(0.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='', flush=True)

def slow() -> int:
    time.sleep(10)        
    return 42

def supervisor() -> int:
    done = Event()
    spinner = Process(target=spin,
                      args=['THINKING...', done])
    print(f'spinner object: {spinner}')
    spinner.start()
    res = slow()
    done.set()
    spinner.join()
    return res

def main() -> None:
    res = supervisor()
    print(f'Answer: {res}') 

if "__main__" == __name__:
    main()    