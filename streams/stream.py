import asyncio

"""
Stream
    流是用于处理网络连接的支持async/await的高层级原语.流允许发送、接收数据，而不需要使用回调或低级协议和传输. 
"""
async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        "127.0.0.1", 8888 
    )
    
    print(f"Send: {message!r}")  
    writer.write(message.encode())
    await writer.drain()
    
    data = await reader.read(100)    
    print(f"Received: {data.decode()!r}")
    
    print("Close the connection...")
    writer.close()
    await writer.wait_closed()
    
asyncio.run(tcp_echo_client("Hi! Claude Code!~✨"))    