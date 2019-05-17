#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# Author: Andrew.zhan
# Create by 2019 Apr 30
import time
import os
import string
import random


def practice_1():
    '''
    1、计算两个格式化时间之间差了多少年月日时分秒
    '''
    date_time_1 = "2019-4-30 12:37:22"
    date_time_2 = "2008-8-8 13:30:36"
    struct_date_time_1 = time.strptime(date_time_1, "%Y-%m-%d %H:%M:%S")
    struct_date_time_2 = time.strptime(date_time_2, "%Y-%m-%d %H:%M:%S")
    time_stamp_1 = time.mktime(struct_date_time_1)
    time_stamp_2 = time.mktime(struct_date_time_2)
    # 因为一会儿要减UTC时间,所以使用gmtime.否则还需要计算时区.
    diff_time = time.gmtime(abs(time_stamp_1 - time_stamp_2))
    # 因为时间戳是1970-01-01 00:00:00开始的. 所以减去这个初始时间就是日期差.
    years = diff_time.tm_year - 1970
    months = diff_time.tm_mon - 1
    days = diff_time.tm_mday - 1
    hours = diff_time.tm_hour
    minutes = diff_time.tm_min
    seconds = diff_time.tm_sec
    print("时间相差%s年%s个月%s天 %s小时%s分%s秒" % (years, months, days, hours, minutes, seconds))


def practice_2():
    '''
    2、计算当前时间所在月1号的时间戳
    '''
    now_time = time.localtime()
    struct_first_day_time = time.strptime(
                                time.strftime("%Y-%m-1 %H:%M:%S", now_time),
                                "%Y-%m-%d %H:%M:%S"
                            )
    print(struct_first_day_time)
    first_day_time_stamp = time.mktime(struct_first_day_time)
    print(first_day_time_stamp)


def practice_3():
    '''
    3、生成一个6位随机验证码(包含数字和大小写字母)
    '''
    source_words = string.ascii_letters + "".join(str(i) for i in range(10))
    result = "".join(random.choices(source_words, k=6))
    return result


def practice_4():
    '''
    4、发红包、制定金额和个数随机分配红包金额
    '''
    # 为了保证剩余人数至少每人可以分到1分钱, 并且为了避免分位值差距过大, 所以计算得到随机区间的max值为剩余金额的50%.
    def get_max(remain, part):
        avg = remain / part
        if avg < 0.02:
            return float("%.2F" % (avg * 1.3))
        # return (remain - (part - 1) * 0.01) * 0.5       # 如果想让红包平均一些,不要让分位值差距过大.那么启用这条.
        return (remain - (part - 1) * 0.01) * float("%.2F" % random.random())    # 如果想玩儿刺激的,那么启用这条.

    # 红包大小与份数, 这章学习重点不在用户输入上, 所以这里简单直接赋值了.
    total = remain = 1000
    count = 5

    # 如果每人都不够平均分到1分钱,那么说明红包太小了.
    if total / count < 0.01:
        print("红包太小不够分.")
        return False

    # 主逻辑入口
    prize_pool = []  # 红包分部池. 一会儿要用到.
    for i in range(count, 0, -1):
        if i == 1:
            prize_pool.append(float("%.2F" % remain))    # 将最后剩余的部分添加到红包池内
            break
        min = 0.01
        max = get_max(remain, i)
        prize = float("%.2F" % random.uniform(min, max))
        remain = remain - prize
        prize_pool.append(prize)     # 将随机出来的金额放到红包池内.

    # 用生成器吐红包, 实现拿一个少一个. 原始列表可以另做其它用途, 例如记录日志.
    get_gold = (i for i in prize_pool)

    # 至此,红包池制作完成. 虽然每个红包大小是随机生成的, 但是因为在循环中remain是递减的, 所以大红包出现的机率也是递减的.
    # 如果直接将这个红包池分配个抢红包的用户, 那么就会出现先抢到的人得到大红包的机率就会高. 最后得机率就会少.
    # 所以在这里,将红包池重新洗牌. 顺序弹出就可以了.
    random.shuffle(prize_pool)

    print("红包池内共: %s (由于精度限制,有可能会出现小数精度不准确的情况,这里不做处理,看效果)\n随机分为: %s份\n" % (sum(prize_pool), count))
    for i in get_gold:
        print("抢到: %s 元" % i)


def practice_5():
    '''
    5、分别列出给定目录下所有的文件和文件夹
    '''
    # os.walk的方式, 我比较喜欢用这个, 很方便.
    def mode_1():
        for i in os.walk('/etc'):
            print(i[0])
            for p in i[2]:
                print(os.path.join(i[0], p))

    # 展开结构的显示类型
    def mode_2():
        def recursive_tree(location, indentation=0):
            dirs = []
            files = []
            # 列出当前目录内的所有文件, 把文件和目录添加到相应的列表内. (加的为绝对路径)
            for i in os.listdir(location):
                _path = os.path.join(location, i)
                if os.path.isfile(_path):
                    files.append(_path)
                if os.path.isdir(_path):
                    dirs.append(_path)
            if indentation == 0:
                print(location)    # 第一层时,打印遍历树的根路径.
            else:
                print(" " * indentation + "- " + os.path.basename(location))     # 第二层开始 为了缩进好看, 打印相对路径(即目录名)
            indentation += 1
            for f in files:
                print(" " * indentation + os.path.basename(f))       # 当前层内的文件,打印出来.
            for d in dirs:
                recursive_tree(d, indentation)                       # 如果当前层内还有目录,那么递归下去继续遍历.

        # 遍历一棵树
        recursive_tree("/etc")

    # mode_1()
    mode_2()


def practice_6():
    '''
    6、获取当前文件所在目录
    '''
    file_path = "/etc/passwd"
    return os.path.dirname(file_path)


def practice_7():
    '''
    7、在当前目录下创建一个文件夹、在这个文件夹下创建一个文件
    '''
    dir_name = "test_dir"
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    os.chdir(dir_name)
    with open("test.txt", 'w', encoding="utf-8") as fp:
        fp.write("abc\n")


def practice_8():
    '''
    8、计算某路径下所有文件和文件夹的总大小
    '''
    total = 0
    for i in os.walk('/etc'):
        for p in i[2]:
            size = os.stat(os.path.join(i[0], p))
            total += size.st_size
    print("%s B" % total)            # 单位我就不换算.


def main():
    # practice_1()
    # practice_2()
    # print(practice_3())
    practice_4()
    # practice_5()
    # print(practice_6())
    # practice_7()
    # practice_8()


if __name__ == "__main__":
    main()

