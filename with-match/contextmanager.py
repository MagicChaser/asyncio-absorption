import contextlib
import sys

@contextlib.contextmanager
def looking_glass():
    # mirror_gen.py使用生成器实现上下文管理器
    original_write = sys.stdout.write
    
    def reverse_write(text):
        original_write(text[::-1])
        
    sys.stdout.write = reverse_write # type: ignore
    yield "Mirror是由a16z的前合伙人Denis Nazarov 创建"
    sys.stdout.write = original_write

def f1():
    # 测试驱动looking_glass上下文管理器函数
    with looking_glass() as what:
        print(what)          
        print("Alice, Kitty and Snowdrop") 
    print(what)    
    print("Back to home.")
"""
建创 vorazaN sineD人伙合前的z61a由是rorriM
pordwonS dna yttiK ,ecilA
Mirror是由a16z的前合伙人Denis Nazarov 创建
Back to home.
"""    

@contextlib.contextmanager
def mirror_gen():
    # 基于生成器的上下文管理器[可以实现异常处理]
    original_write = sys.stdout.write
    
    def reverse_write(text):
        original_write(text[::-1])
    
    sys.stdout.write = reverse_write # type: ignore
    msg = ''
    try:
        yield "Mirror是由a16z的前合伙人Denis Nazarov 创建的一款去中心化内容创作平台"
    except ZeroDivisionError:
        msg = "Please don't divide by zero!"
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)
    
                
def main():
    looking_glass()
    #f1()
    #f2()
    
if "__main__" == __name__:    
    # @contextmanager，是一个巧妙实用的工具，将Python的三个不同功能结合在一起：装饰器、生成器、with语句。它允许我们使用生成器来定义一个上下文管理器，从而简化了资源管理的代码。
    main()