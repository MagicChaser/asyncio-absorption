
"""
Stream函数
    下面的高级asyncio函数可用来创建和处理流.
    1.coroutine asyncio.open_connection(host=None, port=None, *, limit=None, ssl=None, family=0, proto=0, flags=0, sock=None, local_addr=None, server_hostname=None, ssl_handshake_timeout=None, happy_eyeballs_delay=None, interleave=None)
    建立网络连接并返回一对(reder, writer)对象.
    返回的reader和writer对象是StreamReader,StreamWriter类的实例.
    limit确定返回的StreamReader实例使用的缓冲区大小限制.默认为64KiB.
    余下的参数将会直接传递给loop.create_connection()
    2.coroutine asyncio.start_server(client_connected_db, host=None, port=None, *, limit=None, family=socket.AF_UNSPEC, flags=socket.AI_PASSIVE, sock=None, backlog=100, ssl=None, reuse_address=None, reuse_port=None, ssl_handshake_timeout=None, start_serving=True)
    启动套接字服务.
    当一个新的客户端连接被建立时，回调函数client_connected_db会被调用.此函数会接收到一对参数(reader, writer),reader是类StreamReader的实例，而writer是类StreamWriter的实例.
    client_connected_db:可以是普通的可调用对象也可以是一个协程函数.若是写成函数，将自动作为Task被调度.
    limit确定返回的StreamReader实例使用的缓冲区大小限制.同上.
    余下参数将直接传递给loop.create_server()
    3.StreamReader[class asyncio.StreamReader]    
    代表一个提供从IO流读取数据的API的读取器.作为一个asynchronous iterable, 此对象支持async for语句.
    不推荐直接使用实例化StreamReader对象，而是使用open_conection(),start_server()来获取StreamReader实例.
    - coroutine read(n=-1)
        从流读取至多n个字节.未提供或-1,则一直读取到EOF;为0,则立即返回空bytes对象.
    - coroutine readline()
        读取一行.以\n结尾的字节序列.读取EOF，且缓冲区为空，则返回空bytes对象.
    - coroutine readexactly(n)
        精确读取n个bytes,不会超过也不少于.
    - coroutine readuntil(separator=b'\n')
        从流中读取数据直到遇到separator
    4.StreamWriter[class asyncio.StreamWriter]
    这个类表示一个写入器对象，此对象提供api以便写数据至IO流中.
    不建议直接实例化StreamWriter;而应使用open_connection()与start_server().
    - write(data)
        此方法会尝试立刻将data写入到下层的套接字.若写入失败，数据会被排入内容写缓冲队列直到可以被发送.
        # 应当与drain()方法一起配合使用
    - writelines(data)
        此方法会立刻尝试将一个字节串列表(或任何可迭代对象)写入下层的套接字.若写入失败，数据会被排入内部写缓存队列直到可以被发送.
        # 应当与drain()方法一起配合使用
    - close()
        此方法会关闭流以及下层的套接字.
        此方法应当与wait_closed()一起配合使用.但非强制要求.
    - coroutine drain()
        等待直到可以适当地恢复写入到流.如：
        writer.write(data)
        await writer.drain()
        这是一个与下层的IO写缓冲区交互的流程控制方法.当缓冲区大小达到最高水位(最大上限)时，drain()会阻塞直到缓冲区大小减少至最低水位以便恢复写入.当没有要等待的数据时，drain()会立即返回.
    - coroutine wait_closed()
        等待直到流被关闭.
        应当在close()之后调用以等待直到下层连接被关闭，确保所有数据在退出程序之前已刷新.
    示例：使用流的TCP回显客户端.
"""

import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        "127.0.0.1", 8888)      
    print(f"Send: {message!r}")
    writer.write(message.encode())
    
    data = await reader.read(100)
    print(f"Received: {data.decode()!r}")
    
    print('Close the connection.')
    writer.close()
    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(tcp_echo_client("Beautiful soup..."))
# 刚刚上一个例子中writer.write(..)下一行语句有写drain,但这个没写，不过刚刚执行也正常，如何理解？