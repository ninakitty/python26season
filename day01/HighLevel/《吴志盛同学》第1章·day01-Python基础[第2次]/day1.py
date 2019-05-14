1.简述变量命名规范
由数字，字母，下划线任意组合
不能以数字开头
不能有关键字如：
【and ,as ,in,is,for,try,break,class,continue,def,else,execpt,exec,finally,from,global,if,import,lambda,not,or,pass,print,raise,return,while,with】
规范需求：别用中文，拼音

2、name = input(“>>>”) name变量是什么数据类型？
字符串


3、if条件语句的基本结构？
（一）
if  条件： 
	执行语句
（二）
if 条件：
	执行语句
else:
	执行语句
（三）
if 条件：
	执行语句
elif 条件：
	执行语句：
else:


4、用print打印出下面内容：
poetry='''
文能提笔安天下,
武能上马定乾坤.
心存谋略何人胜,
古今英雄唯是君.
'''
print (poetry)

5、利用if语句写出猜大小的游戏：
guess=int(input("请猜一个数字："))
if guess > 66:
    print ('猜测的结果大了')
elif guess == 66:
    print ('猜测结果正确')
else:
    print ('猜测的结果小了')

6、提示用户输入他的年龄, 程序进判断.
ages=int(input('请您输入年龄：'))
if ages >= 90:
    print ('再见了这个世界')
elif ages >= 70:
    print ('人生就快结束了的一个老屁孩儿')
elif ages >= 60:
    print ('活着还不错的老屁孩儿')
elif ages >= 50:
    print ('自己马上变成不听 话的老屁孩儿')
elif ages >= 40:
    print ('家里有个不听话的小屁孩儿')
elif ages >= 30:
    print ('体制看老大不小了, 赶紧结婚小屁孩儿')
elif ages >= 20:
    print ('开始定性, 开始混社会的小屁孩儿')
elif ages >= 10:
    print ('青春期叛逆的小屁孩')
else:
    print ('小屁孩')

	
7、单行注释以及多行注释？
单行注释  #
多行注释 """  """ 或 ''' '''


8、简述你所知道的Python3x和Python2x的区别？
python3
源码优美，清晰，简单
utf-8 : 含各种语言,支持汉语

python2
源码冗余，重复，不规范
ASCII :只含英文
支持汉语：#_*_coding:utf-8_*_


print打印
py2：print语句,可以直接跟要打印的东西

py3：print函数,要加上括号才能调用

输入函数
py2：input_raw()
py3：input()

编码
py2：默认编码ascii
py3：默认编码utf-8


字符串
py2：unicode类型表示字符串序列，str类型表示字节序列
py3:：str类型表示字符串序列，byte类型表示字节序列

True和False
py2：True 和 False 在 Python2 中是两个全局变量，可以为其赋值或者进行别的操作，初始数值分别为1和0，虽然修改是违背了python设计的原则，但是确实可以更改

py3：修正了这个变量，让True或False不可变


9、提示用户输入麻花藤. 判断用户输入的对不对. 如果对, 提示真聪明, 如果不对, 提示你 是傻逼么
name=input('请输入用户名：')
if name == '麻花藤':
    print ('真聪明')
else:
    print('你 是傻逼么')

10、使用while循环输入 1 2 3 4 5 6  8 9 10
number=1
while number <  11:
    if number == 7:
        print (' ')
    else:
        print(number)
    number=number+1

11、求1-100的所有数的和	
number=1
sum=0
while number <= 100:
    sum=number+sum
    number=number+1
print (sum)


12、输出 1-100 内的所有奇数
number=1
sum=0
while number <= 100:
    sum=number+sum
    number=number+2
print (sum)


13、输出 1-100 内的所有偶数
number=0
sum=0
while number <= 100:
    sum=number+sum
    number=number+2
print (sum)


14、求1-2+3-4+5 ... 99的所有数的和
number1=1
number2=2
sum1=0
sum2=0

while number1 <= 100:
    while number2 <= 100:
        sum1=sum1+number1
        sum2=sum2+number2
        number1=number1+2
        number2=number2+2
print (sum1-sum2)
















