import time
from multiprocessing import Process
from threading import Thread

def f1():
    pass


if __name__ == '__main__':
    s_time = time.time()
    t_list = []
    for i in range(100):
        t = Thread(target=f1,)
        t.start()
        t_list.append(t)
    [tt.join() for tt in t_list]
    e_time = time.time()

    ps_time = time.time()
    p_list = []
    for i in range(100):
        p = Process(target=f1,)
        p.start()
        p_list.append(p)
    [pp.join() for pp in p_list]
    pe_time = time.time()

    print('线程创建耗费时间>>',e_time - s_time)
    print('进程创建耗费时间>>',pe_time - ps_time)




