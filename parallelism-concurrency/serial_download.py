import time
from pathlib import Path
from typing import Callable
import httpx 

POP20_CC = ('CH IN US BR RU JP MX DE FR GB CA AU BE CN ES IT KR NL SE').split()

BASE_URL = 'http://localhost:8000/flags'
DEST_DIR = Path('downloads')
DEST_DIR.mkdir(exist_ok=True)

def save_flag(img: bytes, filename: str) -> None:
    (DEST_DIR / filename).write_bytes(img)
    
def get_flag(cc: str) -> bytes:
    url = f"{BASE_URL}/{cc}.png"
    # 本地测试服务器，禁用代理
    with httpx.Client(trust_env=False,
                      timeout=6,
                      follow_redirects=True) as client:
        resp = client.get(url)
        resp.raise_for_status()
        return resp.content

def download_many(cc_list: list[str]) -> int:
    for cc in sorted(cc_list):
        img = get_flag(cc)
        save_flag(img, f"{cc}.gif")
        print(cc, end=' ', flush=True)
    return len(cc_list)

def main(downloader: Callable[[list[str]], int]) -> None:
    DEST_DIR.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    count = downloader(POP20_CC) # type: ignore
    elapsed = time.perf_counter() - t0
    print(f"\n{count} downloads in {elapsed:.2f}s")
    
if __name__ == '__main__':
    main(download_many)  
    
    