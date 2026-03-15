from concurrent import futures
from serial_download import save_flag, get_flag, main

def download_one(cc: str):
    img = get_flag(cc)
    save_flag(img, f"{cc}.gif")
    print(cc, end=' ', flush=True)
    return cc

# def download_many(cc_list: list[str]) -> int:
#     with futures.ThreadPoolExecutor() as executor:
#         res = executor.map(download_one, sorted(cc_list))
#     return len(list(res))

def download_many(cc_list: list[str]) -> int:
    cc_list = cc_list[:10]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do: list[futures.Future] = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            print(f"Scheduled for {cc}: {future!r}")
        for count, future in enumerate(futures.as_completed(to_do), 1):
            res: str = future.result()
            print(f"{future} result: {res!r}")
    return count
    
    
if __name__ == '__main__':
    main(download_many)
"""
(fastapi-py312) blackcat@Admin:~/asyncio-absorption$ python parallelism-concurrency/concurrent_download.py 
BR AU BE CH ES DE CN FR GB IN IT JP KR MX NL RU CA US SE 
19 downloads in 2.44s

(fastapi-py312) blackcat@Admin:~/asyncio-absorption$ python parallelism-concurrency/concurrent_download.py 
Scheduled for BR: <Future at 0x7f67728d19d0 state=running>
Scheduled for CH: <Future at 0x7f67727ec410 state=running>
Scheduled for DE: <Future at 0x7f67727ec9e0 state=running>
Scheduled for FR: <Future at 0x7f67727ecfb0 state=pending>
Scheduled for GB: <Future at 0x7f67727ed040 state=pending>
Scheduled for IN: <Future at 0x7f67727ed100 state=pending>
Scheduled for JP: <Future at 0x7f67727ed1c0 state=pending>
Scheduled for MX: <Future at 0x7f67727ed280 state=pending>
Scheduled for RU: <Future at 0x7f67727ed340 state=pending>
Scheduled for US: <Future at 0x7f67727ed400 state=pending>
DE <Future at 0x7f67727ec9e0 state=finished returned str> result: 'DE'
BR <Future at 0x7f67728d19d0 state=finished returned str> result: 'BR'
CH <Future at 0x7f67727ec410 state=finished returned str> result: 'CH'
FR <Future at 0x7f67727ecfb0 state=finished returned str> result: 'FR'
GB <Future at 0x7f67727ed040 state=finished returned str> result: 'GB'
IN <Future at 0x7f67727ed100 state=finished returned str> result: 'IN'
JP <Future at 0x7f67727ed1c0 state=finished returned str> result: 'JP'
MX <Future at 0x7f67727ed280 state=finished returned str> result: 'MX'
RU <Future at 0x7f67727ed340 state=finished returned str> result: 'RU'
US <Future at 0x7f67727ed400 state=finished returned str> result: 'US'

10 downloads in 1.10s

"""
    
    