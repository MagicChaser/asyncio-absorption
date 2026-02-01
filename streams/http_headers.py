import asyncio
import urllib.parse
import sys

# 获取HTTP标头：查询命令行传入URL的http标头的简单示例.

async def print_http_headers(url):
    url = urllib.parse.urlsplit(url)
    if url.scheme == 'https':
        reader, writer = await asyncio.open_connection(
            url.hostname, 443, ssl=True
        )
    else:
        reader, writer = await asyncio.open_connection(
            url.hostname, 80
        )
    
    query = (
        f"HEAD {url.path or '/'} HTTP/1.0\r\n"
        f"Host: {url.hostname}\r\n"
        f"\r\n"
    )
    
    writer.write(query.encode('latin-1'))
    while True:
        line = await reader.readline()
        if not line:
            break
        
        line = line.decode('latin-1').rstrip()
        if line:
            print(f"HTTP header> {line}")

    # Ignore the body, close the socket.
    writer.close()
    await writer.wait_closed()
    
async def main():
    url = sys.argv[1]
    await print_http_headers(url)

if __name__ == '__main__':
    asyncio.run(main())
    
    
"""
执行结果
(data_pipeline) blackcat@Admin:~/asyncio-absorption$ python -m streams.http_headers https://www.baidu.com
HTTP header> HTTP/1.0 200 OK
HTTP header> Cache-Control: private, no-cache, no-store, proxy-revalidate, no-transform
HTTP header> Content-Length: 0
HTTP header> Content-Type: text/html
HTTP header> Pragma: no-cache
HTTP header> Server: bfe
HTTP header> Date: Thu, 08 Jan 2026 07:26:36 GMT
"""    