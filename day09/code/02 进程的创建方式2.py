
from multiprocessing import Process

class MyProcess(Process):

    def __init__(self,n):
        self.n = n
        super().__init__()

    #这是需要执行的代码逻辑
    def run(self):
        print(self.n)
        print('xxxxxx')

if __name__ == '__main__':
    p = MyProcess(20)
    p.start()
    print('主进程结束')











