import concurrent.futures
import time

num_list = {1,2,3,4,5,6,7,8,9,10}

def evaluate_item(x):
    # 计算总和，此处仅为了消耗时间
    res_item = count(x)
    return res_item
    
def count(n):
    s = 0
    for i in range(0, 10000):
        s = s + i
    return s * n

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evaluate_item, item) for item in num_list]
        # 获取结果
        for future in concurrent.futures.as_completed(futures):
            print(future.result())