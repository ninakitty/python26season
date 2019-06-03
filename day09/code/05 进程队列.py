import time
from multiprocessing import Process,Queue


q = Queue(3)  #先进先出

# q.put('a') #put('a')往队列放数据
# print(q.full()) #False
# print(q.empty()) #False表示非空,True表示空了
# q.put('b')
# q.put('c')
# # q.put('d') # 放多了也会阻塞程序
# # while 1:
# #     try:
# #         q.put_nowait('d') #queue.Full
# #         break
# #     except Exception:
# #         print('队列满啦,别放了,先去干点别的')
# #         print(q.get())
# print(q.full()) #True表示满了,False表示没有满
#
# print('取数据')
# print(q.get()) #get()取数据
# print(q.get())
# print(q.get())
# # print(q.get()) #get多了也会阻塞程序
# try:
#     print(q.get_nowait()) #queue.Empty错误
#
# except Exception:
#     print('队列已经空了,去干别的吧')
#
# print(q.empty())
#
# print('取完了!!!')


# q.put('a') #put('a')往队列放数据
# q.put('b')
# print(q.qsize())
# q.put('c')
# print(q.qsize())
# print(q.full()) #
# q.get()
# q.get()
# q.get()
# q.put('ddd')
# print(q.empty()) #True 异步

































