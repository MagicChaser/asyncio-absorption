import asyncio

async def handle_echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print(f"Received: {message!r} from {addr!r}")
    
    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()
    
    print("Close the connection")
    writer.close()
    await writer.wait_closed()
    
async def main():
    server = await asyncio.start_server(
        client_connected_cb=handle_echo,
        host="127.0.0.1",
        port=8888
    )
    
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f"Serving on {addrs}")   
    
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
    
    
    