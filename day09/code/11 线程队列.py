
import queue
# q = queue.Queue(3) #先进先出
# q.put(1)
# q.put(2)
# q.put(3)
#
# print(q.get())
# print(q.get())
# print(q.get())

#先进后出
# q = queue.LifoQueue()
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())
# print(q.get())
# print(q.get())

#优先级队列 数字越小优先级越高 优先级数字相同的,比较的值,值的类型不一样,会报错
# q = queue.PriorityQueue()
# q.put((3,'你好1'))
# q.put((1,'b好211'))
# q.put((1,{'aa':'bb'}))
# q.put((2,'你好3'))
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())






