#!/usr/bin/env python3
"""
极简版国旗下载测试服务器
用于练习《Fluent Python》中的并发/异步下载示例
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import time

class FlagRequestHandler(SimpleHTTPRequestHandler):
    """支持可配置延迟的请求处理器"""

    def do_GET(self):
        # 打印请求信息，方便观察并发效果
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] {self.address_string()} - {self.path}")

        # 模拟网络延迟（0.1秒），让并发效果更明显
        time.sleep(0.1)

        return super().do_GET()

    def log_message(self, format, *args):
        # 禁用默认日志，我们自定义了打印
        pass


def run_server(port=8000):
    """启动测试服务器"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, FlagRequestHandler)

    print(f"=" * 50)
    print(f"测试服务器启动成功！")
    print(f"访问地址: http://localhost:{port}")
    print(f"按 Ctrl+C 停止服务器")
    print(f"=" * 50)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
        httpd.shutdown()


if __name__ == "__main__":
    run_server()
