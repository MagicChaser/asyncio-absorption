#!/usr/bin/env python3
"""
生成测试用的"国旗"图片
纯色PNG图片，文件名用国家代码
"""

from PIL import Image

# 定义一些国家代码和对应的颜色
FLAGS = {
    "CN.png": (255, 0, 0),      # 中国 - 红
    "US.png": (0, 0, 255),      # 美国 - 蓝
    "JP.png": (255, 255, 255),  # 日本 - 白
    "DE.png": (0, 0, 0),        # 德国 - 黑
    "FR.png": (0, 0, 255),      # 法国 - 蓝
    "GB.png": (255, 0, 0),      # 英国 - 红
    "IT.png": (0, 255, 0),      # 意大利 - 绿
    "KR.png": (0, 0, 255),      # 韩国 - 蓝
    "BR.png": (0, 255, 0),      # 巴西 - 绿
    "IN.png": (255, 165, 0),    # 印度 - 橙
    "RU.png": (0, 0, 255),      # 俄罗斯 - 蓝
    "CA.png": (255, 0, 0),      # 加拿大 - 红
    "AU.png": (0, 0, 255),      # 澳大利亚 - 蓝
    "ES.png": (255, 255, 0),    # 西班牙 - 黄
    "MX.png": (0, 128, 0),      # 墨西哥 - 绿
    "NL.png": (255, 0, 0),      # 荷兰 - 红
    "SE.png": (0, 0, 255),      # 瑞典 - 蓝
    "CH.png": (255, 0, 0),      # 瑞士 - 红
    "BE.png": (0, 0, 0),        # 比利时 - 黑
    "AT.png": (255, 0, 0),      # 奥地利 - 红
}

IMG_SIZE = (200, 120)  # 国旗尺寸

def generate_flags():
    """生成测试用的国旗图片"""
    import os

    # 创建 flags 目录
    os.makedirs("flags", exist_ok=True)

    print("正在生成测试国旗图片...")
    for filename, color in FLAGS.items():
        img = Image.new("RGB", IMG_SIZE, color)
        img.save(f"flags/{filename}")
        print(f"  已生成: {filename}")

    print(f"\n完成！共生成 {len(FLAGS)} 张图片到 flags/ 目录")


if __name__ == "__main__":
    generate_flags()
