import concurrent.futures
import time

# 模拟耗时任务函数
def check_ping(ip):
    print(f"正在检查 {ip}...")
    time.sleep(1)

    if ip in ["192.168.1.1", "192.168.1.2"]:
        print(f"{ip} 存活.")
        return True
    else:
        print(f"{ip} 不存活.")
        return False


ips = ["192.168.1.1", "10.0.0.1", "192.168.1.2", "8.8.8.8"]

# 1.创建线程执行器
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # 2.提交任务并收集future对象
    future_to_ip = {executor.submit(check_ping, ip): ip for ip in ips}

    # 3.遍历已完成的future对象
    print("\n---任务已开始---")
    
    # 加入wait查看变化
    concurrent.futures.wait(future_to_ip, return_when=concurrent.futures.ALL_COMPLETED)
    for future in concurrent.futures.as_completed(future_to_ip):
        ip = future_to_ip[future]
        try:
            # 4.获取任务结果
            res = future.result()
            print(f"IP {ip}检查完毕，结果：{res}")
        except Exception as e:
            print(f"IP {ip}检查时发生异常：{e}")
    print("\n---所有任务执行完毕---")
