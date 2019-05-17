# lwm-005
# 练习题：
# 1.计算两个格式化时间之间差了多少年月日时分秒；
"""
import time
s1 = time.strptime('2018-08-15 00:00:00','%Y-%m-%d %H:%M:%S')
s2 = time.strptime('2018-08-16 00:00:00','%Y-%m-%d %H:%M:%S')
print(s1)
m1 = time.mktime(s1)
m2 = time.mktime(s2)
print(m1,m2)
m3 = m2 - m1
print(m3)
g1 = time.gmtime(m3)
print(g1)
print('过去的年:%s\n月:%s\n日:%s\n时:%s\n分:%s\n秒:%s' % \
      (g1.tm_year-1970,g1.tm_mon-1,g1.tm_mday-1,g1.tm_hour,g1.tm_min,g1.tm_sec))
"""

# 2.计算当前时间所在月1号的时间戳；
"""
import time
def get01():
    str_time = time.strftime('%Y-%m')
    # struct_time = time.strptime(str_time+"-1",'%Y-%m-%d')  #'2018-08-1'
    struct_time = time.strptime(str_time,'%Y-%m')  #'2018-08' '-1 0:0:0'
    return time.mktime(struct_time)

print(get01())
"""


# 3.生成一个6位随机校验码（包含数字和大小写字母);
"""
import random
def func(n=6 ,alph = True):
    ret = ''
    for i in  range(n):
        code = str(random.randint(0,9))
        if alph:
            alph_lower = chr(random.randint(97,122))
            alph_upper = chr(random.randint(65,90))
            code = random.choice([code,alph_lower,alph_upper])
        ret += code
    return ret
print(func())
"""
# 4.发红包、制定金额和个数随机分配红包金额；
"""
import random
res = random.sample(range(1,200 * 100),5 - 1)
res.append(200 * 100)
res.insert(0,0)
res.sort()
print(res)
l = []
for i in range(5):
    l.append((res[i+1] - res[i]) / 100)
print(l)
"""



# 5.分别列出给定目录下所有的文件和文件夹；
"""
import os
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print('root_dir:', root)  # 当前目录路径
        print('sub_dirs:', dirs)  # 当前路径下所有子目录
        print('files:', files)  # 当前路径下所有非目录子文件


file_name('D:\stock_data')
"""


# 6.获取当前文件所在的目录；
"""
import os
print(os.getcwd())
"""

# 7.在当前目录下创建一个文件夹，在这个文件夹下创建一个文件；
"""
import os
File_Path = os.getcwd()[:-4] +'report\\'
    if not os.path.exists(File_Path):
        os.makedirs(File_Path)
"""

# 8.计算某路径下所有文件和文件夹的总大小；
"""
import os

print (os.getcwd())

all_files=os.listdir(os.curdir)
file_dict=dict()

for each_file in all_files:
    if os.path.isfile(each_file):
        file_size=os.path.getsize(each_file)
        file_dict[each_file]=file_size

for each in file_dict.keys():
    print ("%s【%dBytes】" %(each,file_dict[each]))
"""
# 作业：计算器
# import re,sys
'''
要求：
1\实现加减乘除及拓号优先级解析
2\用户输入
- 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
等类似公式后，必须自己解析里面的(),+,-,*,/符号和公式(不能调用eval等类似功能偷懒实现)，
'''
"""
def compute_mul_div(mg):
    '''
    定义一个乘除函数
    :param mg:
    :return:
    '''
    num = mg[0]  #  -40/5
    match = re.search("\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*",num)
    if not match:
        return
    content = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',num).group()
    if len(content.split('*')) > 1:
        v1,v2 = content.split('*')
        value = float(v1) * float(v2)
        # print('v1>>>%s and v2>>>%s'%(str(v1),str(v2)))
        # print('computer_mul:%s and %s'% (str(content),str(value)))
    else:
        v1, v2 = content.split('/')
        value = float(v1) / float(v2)
        # print('v1>>>%s and v2>>>%s' % (str(v1), str(v2)))
        # print('computer_del:%s and %s' % (str(content),str(value)))
    pur,suf = re.split('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',num,1)
    new_str = '%s%s%s'%(pur,value,suf)
    mg[0] = new_str
    #print('pur>>>%s    value>>>%s     uer>>>%s   new_str>>>%s' % (pur, value,suf,new_str))
    compute_mul_div(mg)

def compute_add_sub(mg):
    '''
    运算表达式加减函数
    :param mg:
    :return:
    '''
    while True:
        if mg[0].__contains__('+-') or mg[0].__contains__('++') or mg[0].__contains__('-+') or mg[0].__contains__('--'):
            mg[0] = mg[0].replace('+-', '-')  # 将-替换掉+-
            mg[0] = mg[0].replace('++', '+')  # 将+替换掉++
            mg[0] = mg[0].replace('-+', '-')  # 将-替换掉-+
            mg[0] = mg[0].replace('--', '+')  # 将+替换掉--
        else:
            break
    if mg[0].startswith('-'):  # 如果arg的第0个元素是以-开头
        mg[1] += 1  # arg的第一个元素自加1
        mg[0] = mg[0].replace('-', '&')
        mg[0] = mg[0].replace('+', '-')
        mg[0] = mg[0].replace('&', '+')  # 将-变+，+变-
        mg[0] = mg[0][1:]  # 将arg中第0个元素中前面多出来的符号去掉
    num = mg[0]  # -40/5
    match = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*',num)
    if not match:
        return
    content = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*',num).group()
    if len(content.split('+')) > 1:
        v1, v2 = content.split('+')
        value = float(v1) + float(v2)
        # print('v1>>>%s and v2>>>%s' % (str(v1), str(v2)))
        # print('computer_add:%s and %s' % (str(content),str(value)))
    else:
        v1, v2 = content.split('-')
        value = float(v1) - float(v2)
        # print('v1>>>%s and v2>>>%s' % (str(v1), str(v2)))
        # print('computer_sub:%s and %s' % (str(content),str(value)))
    pur,suf = re.split('\d+\.*\d*[\+\-]{1}\d+\.*\d*',num,1)
    new_str = '%s%s%s'%(pur,value,suf)
    mg[0] = new_str
    compute_add_sub(mg)

def calate(match_group):
    '''
    计算表达式函数
    :param match_group:
    :return:
    '''
    mg = [match_group.strip('()'),0]   # mg = ['-40/5']
    compute_mul_div(mg)     #调用乘除运算函数
    compute_add_sub(mg)     #调用加减运算函数
    if divmod(mg[1],2)[1] == 1:
        result = float(mg[0])
        result *= -1
        #print('divmod_result:%s'%result)
    else:
        result = float(mg[0])
    #print('in the calator-new_str():%s'%mg)
    return result

def kuohao(calculate):
    '''
    取出表达式中括号函数
    :param calculate:
    :return:
    '''
    while True:
        match = re.search('\([^()]+\)',calculate)   #使用正则表达式 取出优先级最高的括号 并计算
        if match:   #如果表达式中有括号
            match_group = match.group() #
            match_result = calate(match_group)  #调用计算函数
            calculate = calculate.replace(match_group,str(match_result)) #将括号计算后的结果替换原参数
        else:   #若表达式中没有括号
            calate(calculate)
            break
    return calate(calculate)

print('\033[33m 欢迎使用计算器 ：\033[0m'.center(50,'-'))
print('例：1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))')
while True:
    calculate_input = input('\033[32m请输入计算的表达式 | (退出:q)>>>\033[0m')
    calculate_input = re.sub('\s*','',calculate_input)
    if calculate_input == 'q':
        exit('程序退出')
    if len(calculate_input) == 0:
        continue
    if re.search('[^\d\+\-\*/\(\)]',calculate_input):   #使用正则表达式判断用户输入是否是数字、"+-*/"、"()"
        print('\033[31m 输入错误，请重新输入!!!\033[0m')
    else:
        result = kuohao(calculate_input)    #调用去除括号的函数
        print('\033[34m 计算结果>>>%s\033[0m'%result)
        print('\033[35m 正确结果>>>%s\033[0m' % eval(calculate_input))
"""
