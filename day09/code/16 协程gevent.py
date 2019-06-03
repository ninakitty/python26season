
#pip install greenlet
#pip install gevent
import gevent
from gevent import monkey;monkey.patch_all()
import time
def f1():
    # gevent.sleep(1)
    time.sleep(1)
    print('任务1')
def f2():
    # gevent.sleep(1)
    time.sleep(1)
    print('任务2')

g1 = gevent.spawn(f1) #异步提交
g2 = gevent.spawn(f2)
gevent.joinall([g1,g2])
print('主任务结束')
# f1()
# f2()






