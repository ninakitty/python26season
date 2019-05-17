''''''
'''
1，启动程序，用户可选择四个选项：登录，注册，购物，退出。
2，用户注册，用户名不能重复，注册成功之后，用户名密码记录到文件中。
3，用户登录，用户名密码从文件中读取，进行三次验证，验证不成功则退出整个程序。
4，用户登录成功之后才能选择购物功能进行购物，购物功能（就是将购物车封装到购物的函数中）。
5，退出则是退出整个程序。
'''
def han2():
    print("欢迎注册:")  # 用户名和密码用 @ 隔开
    while 1:
        username = input("请输入用户名:").strip()
        password = input("请输入密码:").strip()
        if username == "" or password == "":
            print("输出错误,请重新输入:")
            continue
        f = open("用户信息", mode="r+", encoding="utf-8")
        for line in f:
            if username == line.split("@")[0]:
                print("该用户以存在,请重新输入:")
                break
        else:
            f.write("\n" + username + "@" + password)
            print("注册成功!!!")
            break


def han3():
    print("欢迎登陆!!!")
    count = 2
    while count >= 0:
        username = input("请输入用户名:").strip()
        password = input("请输入密码:").strip()
        f = open("用户信息", mode="r", encoding="utf-8")
        for line in f:
            if username == line.split("@")[0] and password == line.split("@")[1]:
                print("登陆成功了呢!")
                break
        else:
            print("用户名或密码输入错误,还有%s次机会:" % (count))
            count -= 1
    else:
        print("已经错误三次,好遗憾,没机会了呢!")


def han4():
    print("欢迎进入商城:")
    l2 = [
        {"name": "电脑", "price": 999},
        {"name": "鼠标", "price": 100},
        {"name": "特斯拉", "price": 3000},
        {"name": "手机", "price": 500},
    ]
    sum = 0
    shop_car = {}
    money = input("请输入您的金额:")
    if money.isdigit():
        while 1:
            for el in range(len(l2)):
                print(el + 1, l2[el]["name"], l2[el]["price"])
            number = input("请输入您所选的商品序号,N/结算,Q/退出:")
            if number.isdigit() and 0 < int(number) <= len(l2):
                number_index = int(number) - 1
                if shop_car.get(number_index) == None:
                    shop_car[number_index] = 1
                else:
                    shop_car[number_index] = shop_car[number_index] + 1
            elif number.upper() == "N":
                for n in shop_car:
                    sum = sum + shop_car[n] * l2[n]["price"]
                if int(money) >= sum:
                    for m in shop_car:
                        print(f"您购买的商品是{l2[m]['name']},单价为{l2[m]['price']},数量是{shop_car[m]}")
                else:
                    print("对不起,您的金额不足!!!")
            elif number.upper() == "Q":
                sum2 = int(money) - sum
                print(f"您一共花费{sum},剩余{sum2}")
                break
            else:
                print("输入有误,请重新输入:")
    else:
        print("请正确输入金额:")


def han5():
    print("再见了,欢迎下次再来!!!")


def han1():
    li = ["注册", "登陆", "购物", "退出"]
    print("欢迎进入新世界购物系统:")
    for i in range(len(li)):
        print(i + 1, ".", li[i])
    a = input("请输入所要进入功能序号:")
    if a.isdigit():
        if int(a) == 1:
            han2()
        elif int(a) == 2:
            han3()
        elif int(a) == 3:
            han4()
        else:
            han5()
    else:
        print("输入有误,请重新输入:")


han1()

'''
http://www.cnblogs.com/zhaoyunlong/p/8658937.html
1、 文件a1.txt内容
序号 部门 人数 平均年龄 备注
1 python 30 26 单身狗
2 Linux 26 30 没对象
3 运营部 20 24 女生多
.......
通过代码，将其构建成这种数据类型：
[{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},......]
'''
lis = []
with open('test1', encoding ='UTF-8',mode='r')as f:
    m = f.readline()  #你readline读取后文件指针就会跑到你读取的后面了
    n = m.split()
    for i in f:  #这个时候你在遍历文件就会排除你readline的第一行了
        dic ={}
        l = i.split()
        for j in range(len(l)) :
            dic[n[j]] = l[j]
        lis.append(dic)
    print(lis)


'''
2、 传入函数的字符串中,[数字]、[字母]、[空格] 以及 [其他]的个数，并返回结果。
'''
def count(s):
    count_a=count_z=count_o=count_s=0
    for i in s:
        if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):
            count_a=count_a+1
        elif ord(i)>=48 and ord(i)<=57:
            count_z=count_z+1
        elif ord(i)==32:
            count_s=count_s+1
        else:
            count_o=count_o+1
    print ("英文字母个数：%d个"%count_a)
    print ("数字个数：%d个"%count_z)
    print ("其他字符个数：%d个"%count_o)
    print ("空格个数：%d个"%count_s)
str=input("请输入字符串")
count(str)

'''
3、 写函数，接收两个数字参数，返回比较大的那个数字。
'''
def size(n,m):
   if n.isdigit() and m.isdigit():
       if n > m  == True:
           print (n)
       else:
           print (m)
number1=input("请输入要比较大小的数字：")
number2=input("请输入要比较大小的数字：")
size(number1,number2)

'''
4、 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容
返回给调用者。
'''
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
def dic1(x):
    for value in dic.values():
        if type(value) == str or type(value) == list:
            if len(value) > 2:
                print(value[:2])
            else:
                print(value)
dic1(dic)


'''
5、 写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一
个字典，此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为
{0:11,1:22,2:33}。
'''
lis=[11,22,33]
def transform(x):
    if type(lis) == list:
         dict={}
         for l in range(len(lis)):
             dict[l]=lis[l]
         print(dict)
transform(lis)

'''
6、 写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这
四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个student_msg文件中
'''
def information(*dic):
    with open("student_msg",mode='a',encoding='utf-8') as f:
        f.write(*dic)
information('姓名，性别，年龄，学历')


'''
8、 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作。
'''
import os
with open('test8',mode='r',encoding='utf-8') as f,\
    open('test8.1',mode='w',encoding='utf-8') as f1:
    for line in f:
        if line.startswith('apple'):
            line=line.replace('10','12')
        f1.write(line)
os.remove('test8')
os.rename('test8.1','test8')



'''
9、 读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
a=10
b=20
def test5(a,b):
    print(a,b)
c = test5(b,a)
print(c)
'''
a=10
b=20
c=None
#a.b的值已经赋值变量了
#c为None是因函数都有返回值
# 不写/只写return ： 没有特意的返回某个值,默认返回None

'''
10、 写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等),将每个实参的每个元素依次
添加到函数的动态参数args里面
例如 传入函数两个参数[1,2,3] (22,33)最终args为(1,2,3,22,33)
'''
def f1(*k):
    print(k)
f1(*[1,2,3],*(22,33))

'''
11、 写函数,传入函数中多个实参(实参均为字典),将每个实参的键值对依次添加到函数的动态参数kwargs
里面.
例如 传入函数两个参数{‘name’:’alex’} {‘age’:1000}最终kwargs为{‘name’:’alex’ ,‘age’:1000}
'''

def f1(**kw):
    print(kw)
f1(**{'name':'alex'},**{'age':1000})

'''
12、 下面代码成立么?如果不成立为什么报错?怎么解决?
'''
#题目一：
a = 2
def wrapper():
    print(a)
wrapper()

#题目二：
a = 2
def wrapper(a):
    a+=1
    print(a)
wrapper(a)

#题目三：
def wrapper():
    a = 1
    def inner():
        print(a)

    inner()
wrapper()

#题目四：
def wrapper():
    a = 1
    def inner(a):
        a += 1
        print(a)

    inner(a)
wrapper()


'''
13、 写函数,接收两个数字参数,将较小的数字返回.
'''
print('first'.center(40, '='))
def num(a,b):
    if a > b:
        return b
    else:
        return a
r = num(1,2)
print(r)

'''
14、 写函数,接收一个参数(此参数类型必须是可迭代对象),将可迭代对象的每个元素以’_’相连接,形成新的字
符串,并返回
例如 传入的可迭代对象为[1,'老男孩','武sir']返回的结果为’1_老男孩_武sir’
'''

def fun(li):
    s = ""
    for i in li:
        s += str(i) + '_'
    print(s.strip("_"),end="")
fun([1,'老男孩','武sir'])

'''
15、 写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
例如：如:min_max(2,5,7,8,4) 返回:{‘max’:8,’min’:2}(此题用到max(),min()内置函数)
'''
def convert(*args):
    dic = {}
    dic['max'] = max(args)
    dic['min'] = min(args)
    return dic
print(convert(2,5,7,8,4))


'''
16、 写函数，传入一个参数n，返回n的阶乘
例如:cal(7) 计算7*6*5*4*3*2*1
'''
def func(n):
    if n == 0:
        return True
    return n * func(n - 1)
a = func(7)
print(a)


'''
17、 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃’，‘A’)]
'''
def poke():
    li = ['黑','红','花','片']
    li1 = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    li2 = []
    for i in li:
        for n in li1:
            li2.append((i,n))
    return li2
print(poke())















