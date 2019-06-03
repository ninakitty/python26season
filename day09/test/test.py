# 进程方法一
# import time, os
# from multiprocessing import Process
#
#
# def func1(n):
#     print(func1.__name__, os.getpid())  # 当前进程号
#     print(func1.__name__, os.getppid())  # 父进程号
#     print(111111111)
#     time.sleep(2)
#     print('---------', n)
#
#
# def func2(n):
#     print(func2.__name__, os.getpid())  # 当前进程号
#     print(func2.__name__, os.getppid())  # 父进程号
#     print(22222222222)
#     time.sleep(2)
#     print('*********', n)
#
#
# if __name__ == '__main__':
#     p1 = Process(target=func1, args=(1,))
#     p2 = Process(target=func2, args=(2,))
#     p1.start()
#     p2.start()
#     print('主进程结束')
#     print('main', os.getpid())  # 当前进程号
#     print('main--father', os.getppid())  # 父进程号

# 进程方法二
# from multiprocessing import Process
#
#
# class MyProcess(Process):
#     def __init__(self, n):
#         self.n = n
#         super().__init__()
#
#     def run(self) -> None:
#         print('--------', self.n)
#
#
# my_process = MyProcess(20)
# my_process.run()
# print('主进程结束')

# requests前期进程抓取文件
# import requests, time
# from multiprocessing import Process
#
# url_list = ['http://k.zol-img.com.cn/sjbbs/7692/a7691515_s.jpg',
#             'http://pic15.nipic.com/20110628/1369025_192645024000_2.jpg',
#             'http://pic37.nipic.com/20140110/17563091_221827492154_2.jpg']
#
#
# def get_content(url, index):
#     conn = requests.get(url)
#     content = conn.content
#     with open(f'tupien{index}.jpg', mode='wb') as fp:
#         fp.write(content)
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#     process_list = []  # 线程列表
#     for index, url in enumerate(url_list):
#         process = Process(target=get_content, args=(url, index))
#         process.start()
#         process_list.append(process)
#     [process.join() for process in process_list]  # 让每个进程完成后等待
#     end_time = time.time()
#     print('时间差:', end_time - start_time)

# 守护进程
# import time
# from multiprocessing import Process
#
#
# def f1(n):
#     print(11111)
#     time.sleep(2)
#     print('>>>>>>', n)
#
#
# def f2(n):
#     print(22222)
#     time.sleep(3)
#     print('!!!!!!', n)
#
#
# if __name__ == '__main__':
#     # 同步(串行)和异步  提交任务的方式
#     # f1()
#     # f2()
#     # 阻塞和非阻塞  任务的执行状态
#     # 进程的三状态 :就绪  运行  阻塞
#
#     #
#     p1 = Process(target=f1, args=(1,))
#     p2 = Process(target=f2, args=(2,))
#     # 设置守护进行,必须start之前
#     p2.daemon = True
#     p1.start()
#     p2.start()
#     time.sleep(1)
#     print('主进程结束')

# 进程间通信
from multiprocessing import Process, Queue

# def f1(q):
#     ret = q.get()
#     print('子进程的ret>>', ret)
#
#
# if __name__ == '__main__':
#     q = Queue(3)
#     q.put('你好')
#     p = Process(target=f1, args=(q,))
#     p.start()
# def fun1(q):
#     result = q.get()
#     print('子进程result>>', result)
#
#
# if __name__ == '__main__':
#     q = Queue(3)
#     q.put('hello')
#     p = Process(target=fun1, args=(q,))
#     p.start()


# 线程创建一
# from threading import Thread
# #
# #
# # def fun1(n):
# #     print(111111111111, n)
# #
# #
# # def fun2(n):
# #     print(222222222222, n)
# #
# #
# # if __name__ == '__main__':
# #     t1 = Thread(target=fun1, args=(10,))
# #     t2 = Thread(target=fun2, args=(20,))
# #     t1.start()
# #     t2.start()
# #     print('主程序结束')

# 线程创建二
# from threading import Thread
#
#
# class MyThread(Thread):
#     def __init__(self, n):
#         super().__init__()
#         self.n = n
#
#     def run(self):
#         print(self.n)
#
#
# if __name__ == '__main__':
#     t1 = MyThread(111)
#     t2 = MyThread(222)
#     t1.start()
#     t2.start()

# 加锁
# import time
# from threading import Thread, Lock
#
# n = 100
#
#
# def func(lock):
#     with lock:  # 为程序加锁
#         global n
#         num = n
#         num -= 1
#         time.sleep(0.1)
#         n = num
#
#
# if __name__ == '__main__':
#     lock = Lock()
#     t_list = []
#     for i in range(10):
#         t1 = Thread(target=func, args=(lock,))
#         t1.start()
#         t_list.append(t1)
#     [thread.join() for thread in t_list]
#     print(n)
#     print('主程序结束')

# 解决死锁，使用RLock
# import time
# from threading import Thread, Lock, RLock
#
#
# def f1(locA, locB):
#     locA.acquire()
#     print('线程1拿到了A锁')
#     time.sleep(1)
#     locB.acquire()
#     print('线程1拿到了B锁')
#     locA.release()
#     locB.release()
#
#
# def f2(locA, locB):
#     locB.acquire()
#     print('线程2拿到了B锁')
#     time.sleep(1)
#     locA.acquire()
#     print('线程2拿到了A锁')
#     locA.release()
#     locB.release()


# if __name__ == '__main__':
#     # locA = Lock()
#     # locB = Lock()
#     # locA = locB = Lock()
#     locA = locB = RLock()
#     t1 = Thread(target=f1, args=(locA, locB))
#     # t2 = Thread(target=f2,args=(locA,locB))
#     t1.start()
#     # t2.start()

# 队列
# import queue
# q = queue.Queue(3)  # 先进先出
# q.put(1)
# q.put(2)
# q.put(3)
#
# print(q.get())
# print(q.get())
# print(q.get())
#
#
# q = queue.LifoQueue(3)  # 先进后出队列
# q.put('11')
# q.put('22')
# q.put('33')
# print(q.get())
# print(q.get())
# print(q.get())
#
#
# q = queue.PriorityQueue(3)  # 优先级队列,按第一位数字排序
# q.put((2, 'i`m 11'))
# q.put((3, 'i`m 33'))
# q.put((1, 'i`m 22'))
#
# print(q.get())
# print(q.get())
# print(q.get())

# 守护线程
# import time
# from threading import Thread
#
#
# def fun1():
#     print('*****')
#     time.sleep(3)
#     print(1111111)
#
#
# def fun2():
#     print('---------')
#     time.sleep(2)
#     print(2222222222)
#
#
# if __name__ == '__main__':
#     t1 = Thread(target=fun1, )
#     t2 = Thread(target=fun2, )
#     t1.daemon = True  # 设置成守护线程,会等待所有线程完成后再结束运行
#     t1.start()
#     t2.start()

# 协程
import time
import gevent
from gevent import monkey

monkey.patch_all()


def fun1():
    time.sleep(1)
    print('11111111')


def fun2():
    time.sleep(1)
    print('2222222')

if __name__ == '__main__':
    gevent.spawn(fun1)
    gevent.spawn(fun2)
