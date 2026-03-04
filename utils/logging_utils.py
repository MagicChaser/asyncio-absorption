from contextlib import contextmanager
import logging
import sys, os
from datetime import datetime

@contextmanager
def temporary_log_level(level: int):
    """临时切换日志级别"""
    logger = logging.getLogger()
    old_level = logger.level
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)
        

def setup_logging(log_file="app.log"):
	# log目录
	log_dir = "logs"
	os.makedirs(log_dir, exist_ok=True)
	log_file = os.path.join(log_dir, f"app_{datetime.now():%Y%m%d}.log")
		
	root = logging.getLogger()
	root.setLevel(logging.INFO)  # 默认INFO
		
	# 格式：时间 + 路径(name:模块名) + 行号
	formatter = logging.Formatter(
			'%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
	)
		
	# 1.终端输出:StreamHandler
	console = logging.StreamHandler(sys.stdout)
	console.setFormatter(formatter)
	root.addHandler(console)
		
	# 2.文件输出:FileHandler
	file_handler = logging.FileHandler(log_file, encoding='utf-8')
	file_handler.setFormatter(formatter)
	root.addHandler(file_handler)
		
	logging.info("日志系统初始化完成：终端 + 文件双输出")        