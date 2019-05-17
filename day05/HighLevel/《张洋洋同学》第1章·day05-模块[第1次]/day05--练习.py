# Yang

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
