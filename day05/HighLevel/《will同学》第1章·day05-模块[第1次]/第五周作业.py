import datetime
import time
import random
import os
#计算两个格式化时间之间差了多少年月日时分秒
def time_dff(date1,date2):
    date1 = datetime.datetime.strptime(date1,'%Y-%m-%d %H:%M:%S')
    date2 = datetime.datetime.strptime(date2,'%Y-%m-%d %H:%M:%S')
    return date2-date1

a = r'2018-02-16 02:35:00'
b = r'2019-02-15 02:24:00'
print(time_dff(a,b))

#计算当前时间所在月1号的时间戳
a = datetime.date(datetime.date.today().year,datetime.date.today().month,1)
print(a)

#生成一个6位随机验证码(包含数字和大小写字母)
def code():
    code1 = ''
    for i in range(6):
        num = random.randint(0,9)
        num1 = chr(random.randint(65,90))
        add = random.choice([num,num1])
        code1 = ''.join([code1,str(add)])
    return code1
print(code())
# 发红包、制定金额和个数随机分配红包金额
def money_dd(money,num):
    try:
        import random
        money *= 100
        money = int(money)
        ret = random.sample(range(1, money - 1), num - 1)
        ret = sorted(ret)
        ret.insert(0, 0)
        ret.append(money)
        ret = [round(ret[i + 1] * 0.01 - ret[i] * 0.01, 2) for i in range(num)]
        random.shuffle(ret)
        return ret
    except ValueError:
        return '输入不规范'
    except TypeError:
        return '输入不规范'

if __name__ == '__main__':
        print(money_dd(10, 5))
        print(money_dd(1, 5))
        print(money_dd(100, 5))


# 分别列出给定目录下所有的文件和文件夹
# import os
# for filename in os.listdir(r'C:\Windows'):
#     print(filename)

# 获取当前文件所在目录
# print(os.getcwd())
# 在当前目录下创建一个文件夹、在这个文件夹下创建一个文件
# import os
# a = 'C:\Windows'
# b = 'hello'
# if os.path.isdir(a):
#     os.mkdir(os.path.join(a,b))
# 计算某路径下所有文件和文件夹的总大小
def get_size(path):
    import os
    if os.path.split(path)[1]:
        size = 0
        if os.path.isfile(path):
            size += os.path.getsize(path)
        elif os.path.isdir(path):
            if os.listdir(path):
                    for path_son in os.listdir(path):
                        path_son = os.path.join(path, path_son)
                        size += get_size(path_son)
            else:
                size += 4096
        return size
    else:
        return '无法计算磁盘大小'


if __name__ == '__main__':
    import os
    print(f'{__file__}文件大小为：', get_size(__file__), '字节')
    print(get_size(os.getcwd()))

#1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
import re
def formats(func):
    def inner(msg):
        msg = msg.replace(' ', '').replace('-+', '-').replace('++', '+').replace('--', '+').replace('++', '+')
        ret = func(msg)
        return ret
    return inner

@formats
def multiply_divide(msg):
    if '*' in msg:
        return str(float(msg.split('*')[0]) * float(msg.split('*')[1]))
    else:
        return str(float(msg.split('/')[0]) / float(msg.split('/')[1]))

@formats
def multiple_multiply_divide(msg):
    if '*' in msg or '/' in msg:
        obj = re.search('\d+(\.\d+)?[*/][-+]?\d+(\.\d+)?', msg).group()
        ret = msg.replace(obj, multiply_divide(obj))
        if msg.count('*') + msg.count('/') > 0:
            return multiple_multiply_divide(ret)
        else:
            return ret
    else:
        return msg

@formats
def add_subtract(msg):
    ret = re.findall('(-?\d+(\.\d+)?)', msg)
    if len(ret) == 1:
        return ret[0][0]
    else:
        ret = (float(i[0]) for i in ret)
        return str(sum(ret))

@formats
def core(msg):
    try:
        eval(msg)
    except:
        '**'
    else:
        if '(' in msg:
            ret = msg
            for i in [(i, add_subtract(multiple_multiply_divide(i))) for i in re.findall('\([^()]+\)', msg)]:
                ret = ret.replace(i[0], i[1])
            if '(' in ret:
                return core(ret)
            else:
                return float(add_subtract(multiple_multiply_divide(ret)))
        else:
            return float(add_subtract(multiple_multiply_divide(msg)))

if __name__ == '__main__':
    msg = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    print(core(msg))

print(1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ))