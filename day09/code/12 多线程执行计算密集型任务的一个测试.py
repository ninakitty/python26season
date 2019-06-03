import time
from threading import Thread
n = 100000
def ff():
    global n
    num = n
    num -= 1
    n = num
if __name__ == '__main__':
    start_time = time.time()
    t_list = []
    for i in range(10000):
        # t = Thread(target=ff,)
        # t.start()
        # t_list.append(t)
    # [tt.join() for tt in t_list]
        ff()
    end_time = time.time()
    print(end_time-start_time) #1.3174421787261963

# tensorflow

