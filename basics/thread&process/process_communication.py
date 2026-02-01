from multiprocessing import Process, Queue
import os, time, random

# 数据写入的进程 通信
def write(q):
    print(f"Process to write: %s" % os.getpid())
    for v in  ['A', 'B', 'C', 'F', 'G']:
        print("Put %s to queue..." % v)
        q.put(v)
        time.sleep(random.randint(1,3))

# 数据读取的进程
def read(q):
    print("Process to read: %s" % os.getpid())
    while True:
        v = q.get(True)
        print("Get %s from queue." % v)

if __name__ == "__main__":
    # 父进程创建Queue,并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))                   
    pr = Process(target=read, args=(q,))               
    # 启动子进程pw, 写入：
    pw.start()
    # 启动子进程pr,读取：
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程为死循环，无法等待结束直接终止
    pr.kill()