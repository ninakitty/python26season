import time
import os
from multiprocessing import Process

def f1(n):
    print('子进程的id号',os.getpid())  #查看当前运行进行的进程id号
    print('父进程id号',os.getppid()) #查看当前运行进行的进程id号
    print(11111)
    time.sleep(6)
    print('>>>>>>',n)
def f2(n):
    print(22222)
    time.sleep(6)
    print('!!!!!!',n)

# f1()
# f2()
if __name__ == '__main__':
    #进程的第一种创建方式
    p1 = Process(target=f1,args=(1,))
    p1.start()  #给操作系统发信号,告诉操作系统,创建一个和我p1一样的真正的进程

    p2 = Process(target=f2,args=(2,))
    p2.start()
    print(os.getpid())  #320
    time.sleep(5)
    print('主进程结束')

























