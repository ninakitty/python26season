#线程池导入
import time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import random

def f(n):
    time.sleep(random.randint(1,3))
    # print(n)
    return n*n




if __name__ == '__main__':

    # pool = ThreadPoolExecutor(max_workers=5)
    pool = ProcessPoolExecutor(max_workers=5)
    ret_list = []
    for i in range(10):
        ret = pool.submit(f,i)  #异步提交任务,f函数名称或者方法名称,i给f函数的参数
        # print(ret.result())  #join
        ret_list.append(ret)

    # pool.shutdown()  #锁定线程池,不让新任务再提交进来了.轻易不用
    for i in ret_list:
        print(i.result())












