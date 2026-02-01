from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print(f"Run task:{name}, {os.getpid}")
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print(f"Task {name} runs {end-start} seconds.")
    
if __name__ == "__main__":
    print("Parent process %s." % os.getpid())
    p = Pool(8)
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))
    p.close()
    p.join()
    print("All subprocess done.")