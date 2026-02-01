import asyncio
import socket

# 注册一个打开的套接字以等待使用流的数据.
# 使用open_connection()函数实现等待直接套接字收到数据的协程.

async def wait_for_data():
    # 获取一个引用到当前事件循环，因为想要访问低阶层APIs.
    loop = asyncio.get_running_loop()
    
    # 创建一对已连接的套接字
    rsock, wsock = socket.socketpair()
    
    # 注册打开套接字来等待数据
    reader, writer = await asyncio.open_connection(sock=rsock)
    
    # 模拟来自网络数据的请求接收
    loop.call_soon(wsock.send, 'abc'.encode())
    
    # 等待数据
    data = await reader.read(100)
    
    # 获取数据完毕：关闭套接字
    print("Received: ", data.decode())
    writer.close()
    await writer.wait_closed()
        
    # 关闭第二个套接字
    wsock.close()
    
asyncio.run(wait_for_data())


"""
执行结果：
(data_pipeline) blackcat@Admin:~/asyncio-absorption$ python -m streams.wait_for_data
Received:  abc
"""
    