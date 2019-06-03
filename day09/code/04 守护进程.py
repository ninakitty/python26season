import time
from multiprocessing import Process

def f1(n):
    print(11111)
    time.sleep(2)
    print('>>>>>>',n)

def f2(n):
    print(22222)
    time.sleep(3)
    print('!!!!!!',n)

if __name__ == '__main__':
    #同步(串行)和异步  提交任务的方式
    #f1()
    #f2()
    #阻塞和非阻塞  任务的执行状态
    #进程的三状态 :就绪  运行  阻塞

    #
    p1 = Process(target=f1,args=(1,))
    p2 = Process(target=f2,args=(2,))
    #设置守护进行,必须start之前
    p1.start()
    p2.daemon = True
    p2.start()

    time.sleep(1)
    print('主进程结束')


#IPC进程通信



