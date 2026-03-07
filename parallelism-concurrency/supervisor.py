from .spinner_thread import slow, spin
from threading import Thread, Event

def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=['thinking!', done])
    print(f"spinner object: {spinner}")
    spinner.start()
    res = slow()
    done.set()
    spinner.join()
    return res

def main() -> None:
    res = supervisor()
    print(f"Answer: {res}")
    
if "__main__" == __name__:
    main()