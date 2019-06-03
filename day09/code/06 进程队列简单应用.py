
from multiprocessing import Process,Queue
def f1(q):
    ret = q.get()
    print('子进程的ret>>',ret)

if __name__ == '__main__':
    q = Queue(3)
    q.put('你好')
    p = Process(target=f1,args=(q,))
    p.start()













