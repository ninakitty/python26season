import time
import os
from threading import Thread

# 线程创建的方式1
def f1(n):
    print(os.getpid())
    time.sleep(2)
    print('子线程1',n)

def f2(n):
    print(os.getpid())
    time.sleep(2)
    print('子线程2',n)

if __name__ == '__main__':

    t1 = Thread(target=f1,args=(1,))
    t2 = Thread(target=f2,args=(2,))
    t1.start()
    t2.start()
    print(os.getpid())
    print('主线程')

# 线程创建的方式2

class MyThread(Thread):
    def __init__(self,n):
        super().__init__()
        self.n = n

    def run(self):
        print(self.n)
        print('子线程')

if __name__ == '__main__':

    t = MyThread('xxxx')
    t.start()
    print('主线程')









