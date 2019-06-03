import time
from threading import Thread,Lock,RLock


def f1(locA,locB):
    locA.acquire()
    print('线程1拿到了A锁')
    time.sleep(1)
    locB.acquire()
    print('线程1拿到了B锁')
    locA.release()
    locB.release()

def f2(locA,locB):
    locB.acquire()
    print('线程2拿到了B锁')
    time.sleep(1)
    locA.acquire()
    print('线程2拿到了A锁')
    locA.release()
    locB.release()

if __name__ == '__main__':
    # locA = Lock()
    # locB = Lock()
    # locA = locB = Lock()
    locA = locB = RLock()
    t1 = Thread(target=f1,args=(locA,locB))
    # t2 = Thread(target=f2,args=(locA,locB))
    t1.start()
    # t2.start()



















