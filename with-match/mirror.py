import sys

class LookingGlass:
    def __enter__(self): 
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write # type: ignore
        return "Mirror是由a16z的前合伙人Denis Nazarov 创建的一款去中心化内容创作平台"
    
    def reverse_write(self, text):
        self.original_write(text[::-1])
    
    def __exit__(self, exc_type, exc_val, traceback):
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print("Please don't divide by zero!")
            return True  # 处理异常，返回True表示异常已被处理，不再传播
            