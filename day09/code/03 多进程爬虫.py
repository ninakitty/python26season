import requests
import time
from multiprocessing import Process

# def f1():
#     ret = requests.get(url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559369648708&di=74b4986bd1048ca224070ca7a45b8e1d&imgtype=0&src=http%3A%2F%2Fs9.sinaimg.cn%2Fmw690%2F006hikKrzy7pzDEQbFe68%26690")
#     tt = ret.content
#     with open('meinv1.jpg','wb') as f:
#         f.write(tt)
#
#
# def f2():
#     ret = requests.get(
#         url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559369819138&di=b55c855e6d1078ee31e1b1b447ca6501&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20180812%2Fca01fb5aba994936a47d5640ed4e48d9.jpeg")
#     tt = ret.content
#     with open('meinv2.jpg', 'wb') as f:
#         f.write(tt)
#

# def f3():
#     ret = requests.get(
#         url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559369818983&di=36ccc51b913cb17d6385502b79818398&imgtype=0&src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2Ff8b28a79d598c9a7597a5bec93cf64b8e2f5589435839-ejtiMv_fw658")
#     tt = ret.content
#     with open('meinv3.jpg', 'wb') as f:
#         f.write(tt)


urls = [
"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559369819138&di=b55c855e6d1078ee31e1b1b447ca6501&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20180812%2Fca01fb5aba994936a47d5640ed4e48d9.jpeg",
"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559369819138&di=b55c855e6d1078ee31e1b1b447ca6501&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20180812%2Fca01fb5aba994936a47d5640ed4e48d9.jpeg",
"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559369818983&di=36ccc51b913cb17d6385502b79818398&imgtype=0&src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2Ff8b28a79d598c9a7597a5bec93cf64b8e2f5589435839-ejtiMv_fw658"

]

def ff(url,i):
    ret = requests.get(url=url)
    tt = ret.content
    with open('meinv%s.jpg'%(i),'wb') as f:
        f.write(tt)

if __name__ == '__main__':
    start_time = time.time()
    p_list = []
    for i,url in enumerate(urls):
        p = Process(target=ff,args=(url,i+1))
        p.start()
        p_list.append(p)
    [pp.join() for pp in p_list]
    # for pp in p_list:
    #     pp.join()
    # start_time = time.time()
    # p1 = Process(target=f1,args=(1,))
    # p2 = Process(target=f2,)
    # p3 = Process(target=f3,)
    # p1.start()
    # p2.start()
    # p3.start()
    # p1.join()
    # p2.join()
    # p3.join()
    end_time = time.time()
    print('并发多进程执行时间:',end_time - start_time)
    #并发多进程执行时间: 0.628286600112915

#串行执行任务
# start_time = time.time()
# f1()
# f2()
# f3()
# end_time = time.time()
# print('串行执行任务的时间',end_time-start_time)
# #串行执行任务的时间 1.1369609832763672





