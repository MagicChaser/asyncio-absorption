
def f1():
    # 示例1：把文件对象当作上下文管理器使用，确保文件关闭
    with open('./with-match/mirror.txt') as fp:
        src = fp.read(30)
    print(len(src))
    print(fp)
    # 30
    # <_io.TextIOWrapper name='./with-match/mirror.txt' mode='r' encoding='UTF-8'>
    print(fp.closed, fp.encoding)
    # True UTF-8
    print(fp.read(60))
    # Traceback (most recent call last):  
    # ValueError: I/O operation on closed file.
    
def f2():
    # 测试驱动LookingGlass上下文管理器类
    from .mirror import LookingGlass
    with LookingGlass() as what:
        print(what)  
        # 台平作创容内化心中去款一的建创 vorazaN sineD人伙合前的z61a由是rorriM
        print("Alice, Kitty and Snowdrop") 
        # pordwonS dna yttiK ,ecilA
        
def f3():
    # with块外使用LookGlass类
    from .mirror import LookingGlass
    manager = LookingGlass()
    print(manager)
    # <with-match.mirror.LookingGlass object at 0x7f5299e33ee0>
    monster = manager.__enter__()
    flg = monster == "Mirror是由a16z的前合伙人Denis Nazarov 创建的一款去中心化内容创作平台"
    print(flg)
    # eurT
    print(monster)
    # 台平作创容内化心中去款一的建创 vorazaN sineD人伙合前的z61a由是rorriM
    print(manager.__exit__(None, None, None))
    # None
    
    
    
            
def main():
    # f1()
    # f2()
    f3()
    
    
if "__main__" == __name__:
    main()