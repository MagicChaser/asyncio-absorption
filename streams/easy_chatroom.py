import asyncio
from faker import Faker
import random

# 简单聊天室：客户端之间相互广播 
userids = ["001", "002", "003", "004"]
fake = Faker()
# 根据多个用户id异步创建任务 -> 建立异步网络客户端连接 -> 循环处理消息广播[生成消息并输出x已发送到y的内容 -> 消息编码写入数据 -> 读取数据 -> 消息解码 -> 输出y已收到x的内容]
async def chat(id):
    reader, writer = await asyncio.open_connection("127.0.0.1", 8888)        
    # 
    message = fake.sentence(nb_words=6 + random.randint(1,6))            
    for userid in userids:  
        if id != userid:                        
            print(f"USER[{id}] Send to USER[{userid}]: '{message}'")
            data = writer.write(message.encode())
            data = await reader.read(n=300)
            message = data.decode()
            print(f"USER[{userid}] Received message from USER[{id}]: '{message}'")
    print(f"USER[{id}] connected closed...")
    writer.close()
    await writer.wait_closed()

async def main():
    tasks = []
    for id in userids:
        task = asyncio.create_task(chat(id))
        tasks.append(task)
    await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main())
    
"""

  问题根源：

  1. 第 32 行缺少 await：res = asyncio.gather(*futures)
    - gather 返回的是协程对象，必须 await 才会真正执行任务
    - 没有 await 导致所有任务都没执行，所以无输出
  2. 第 29 行缺少 tasks.append(task)（你已经加上了）
    - 如果不添加到列表，gather 收集不到任务
  3. try-except 位置错误：
    - create_task 不会抛出异常，异常发生在任务内部
    - 添加 return_exceptions=True 让 gather 捕获任务内的异常

  修改内容（/home/blackcat/asyncio-absorption/streams/easy_chatroom.py:24-29）：
  async def main():
      tasks = []
      for id in userids:
          task = asyncio.create_task(chat(id))
          tasks.append(task)
      await asyncio.gather(*tasks, return_exceptions=True)  # 关键：必须 await

  现在代码能正常运行并输出消息了。
"""    