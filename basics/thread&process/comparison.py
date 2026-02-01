import concurrent.futures
import time

num_list = {1,2,3,4,5,6,7,8,9,10}

def evaluate_item(x):
    # 计算总和，此处仅为了消耗时间  
    res_item = count(x)
    return res_item
    
def count(n):
    for i in range(0, 10000000):
        i = i + 1 
    return i * n

if __name__ == "__main__":
    # 顺序执行
    start_time = time.time()
    for item in num_list:
        print(evaluate_item(item))
    print("Sequential execution in " + str(time.time() - start_time), "seconds")
          
    # 线程池执行
    t_start_time = time.time()      
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
          futures = [executor.submit(evaluate_item, item) for item in num_list]
          for futures in concurrent.futures.as_completed(futures):
              print(futures.result())
    print("Thread pool execution in " + str(time.time() - t_start_time), "seconds")
          
    # 进程池执行
    p_start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evaluate_item, item) for item in num_list]
        # 获取结果
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
    print("Process pool execution in " + str(time.time() - p_start_time), "seconds")