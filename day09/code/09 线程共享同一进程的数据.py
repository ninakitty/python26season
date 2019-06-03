import time
from threading import Thread,Lock

n = 100
def f1(loc):
    with loc:
        # loc.acquire()  #加锁
        global n
        num = n
        num -= 1
        time.sleep(0.001)
        n = num
        # loc.release() #释放锁
if __name__ == '__main__':
    loc = Lock()
    t_list = []
    for i in range(10):
        t = Thread(target=f1,args=(loc,))
        t.start()
        # t.join()
        t_list.append(t)
    [tt.join() for tt in t_list]
    print(n)


