import logging 
from contextlib import contextmanager
from utils import logging_utils 

# 1.定义contextmanager
# @contextmanager
# def temperature_log_level(level: int):
#     """"temp log level"""
#     logger = logging.getLogger()
#     old_level = logger.level
#     logger.setLevel(level)
#     try:
#         yield
#     finally:
#         logger.setLevel(old_level)
# 在level参数前加入一个参数logger_name: str,并在函数内部使用logging.getLogger(logger_name)来获取指定的logger实例


# 2.配置日志！
# 先把根 logger 设置成INFO级别，这样外面默认只看到INFO
# logging.basicConfig(
#     level=logging.INFO,
#     format='[%(levelname)s][%(asctime)s]: %(message)s'  # 设置日志格式
# )

# 3.测试代码
def f1():
    print("1.with块之前:")
    logging.info("这是INFO级别的日志")
    logging.debug("这是DEBUG级别的日志")
    
    print("2.进入with块：")
    with temperature_log_level(logging.WARNING): # type: ignore
        logging.info("这是INFO级别的日志")
        logging.debug("这是DEBUG级别的日志")
        
    print("3.with块之后：")
    logging.info("这是INFO级别的日志")
    logging.debug("这是DEBUG级别的日志")

""" DEBUG输出：
1.with块之前:
INFO: 这是INFO级别的日志
2.进入with块：
INFO: 这是INFO级别的日志
DEBUG: 这是DEBUG级别的日志
3.with块之后：
INFO: 这是INFO级别的日志

WARNING输出：
1.with块之前:
INFO: 这是INFO级别的日志
2.进入with块：
3.with块之后：
INFO: 这是INFO级别的日志

INFO输出：
1.with块之前:
INFO: 这是INFO级别的日志
2.进入with块：
INFO: 这是INFO级别的日志
3.with块之后：
INFO: 这是INFO级别的日志
"""

def f2():
    # 从utils调用            
    logging.info("正常INFO-终端、文件应该都有。")
    
    with logging_utils.temporary_log_level(logging.DEBUG):
        logging.debug("临时DEBUG-终端、文件应该都有。")
        logging.info("临时INFO-终端、文件应该都有。")
    

    
def main():
    # 仅在入口文件顶部调用一次
    logging_utils.setup_logging()
    # f1()
    f2()
    
if __name__ == "__main__":
    main()    
    