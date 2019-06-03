import time
from threading import Thread


def f1():
    print(1111)
    # time.sleep(2)
    time.sleep(3)
    print(22222)

def f2():
    print(3333)
    # time.sleep(3)
    time.sleep(2)
    print(44444)

if __name__ == '__main__':
    t1 = Thread(target=f1,)
    t2 = Thread(target=f2,)
    t1.daemon = True
    t1.start()
    t2.start()
    print('主线程运行结束')








