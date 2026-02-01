import asyncio
import requests
import time
import aiohttp

# 练习：使用gather并发请求10个http接口并统计耗时.

links = [
    "https://www.office.com/",
    "https://www.taobao.com/",
    "https://tieba.baidu.com/index.html",
    "https://www.sogou.com/",
    "https://www.baidu.com/",
    "https://www.qq.com/",
    "https://www.163.com/",
    "https://www.4399.com/",
    "https://www.jd.com/",
    "https://www.douban.com/"
]

async def request(link):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(link, ssl=False) as res:  # ssl=false规避部分ssl兼容问题
                await res.text()
        except Exception as e:
            print(f"请求{link}失败：{str(e)}")
            return    
    end_time = time.time()
    print(f"请求{link}访问时长：{end_time - start_time}s.")

async def main():
    tasks = [request(link) for link in links]
    # 解包tasks放入coros_or_futures参数.
    await asyncio.gather(*tasks)   # 加await等待所有任务完成.

if __name__ == "__main__":
    asyncio.run(main())
 
"""
请求https://www.4399.com/失败：'utf-8' codec can't decode byte 0xd3 in position 310: invalid continuation byte
请求https://www.jd.com/访问时长：0.12433791160583496s.
请求https://www.taobao.com/访问时长：0.12525558471679688s.
请求https://www.baidu.com/访问时长：0.12818002700805664s.
请求https://tieba.baidu.com/index.html访问时长：0.12845587730407715s.
请求https://www.qq.com/访问时长：0.15541744232177734s.
请求https://www.sogou.com/访问时长：0.22527098655700684s.
请求https://www.163.com/访问时长：0.2885162830352783s.
请求https://www.douban.com/访问时长：0.45799851417541504s.
请求https://www.office.com/访问时长：0.5097215175628662s.
"""   