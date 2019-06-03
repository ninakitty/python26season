# 线程池导入
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import random

def f(n):
    time.sleep(random.randint(1, 3))
    return n * n

def call_back(m):
    print(m)
    print(m.result())

if __name__ == '__main__':

    pool = ThreadPoolExecutor(max_workers=5)
    pool.submit(f,2).add_done_callback(call_back)












