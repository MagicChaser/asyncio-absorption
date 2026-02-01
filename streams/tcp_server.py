import asyncio

async def handle_echo(reader, writer):
    """处理客户端连接的回调函数"""
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    
    print(f"Received {message!r} from {addr}")
    
    # 回显消息给客户端
    writer.write(data)
    await writer.drain()
    
    print("Close the client socket")
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8880)
    
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())