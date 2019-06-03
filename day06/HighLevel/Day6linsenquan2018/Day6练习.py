#1.简述类,对象,实例化,实例分别是什么?
'''
类:用来描述具有相同的属性和方法的对象的集合或者是具有相同特征的一类事物.
对象:通过类定义的数据化结构的实例,对象包括俩个数据成员(类变量和实例变量)和方法.
实例化:创建一个类的实例,类的具体对象,也就是类转化成对象的过程.
实例:对象就是一个实例
'''
#2.请简述面向对象三大特性
#3.说说python中封装是什么意思
#4.多态是怎么回事?在python中如何体现
#5.说说面向对象中私有的概念以及应用
#2-5答案如下
'''
a.继承
1)面向对象的编程带来的主要好处之一就是代码的重用,实现这种重用的,实现这种重用的方法
之一就是通过继承机制.
2)继承是一种创新类的方式,新建类可以继承一个或者多个父类,被继承可以称为基类,父类或者超类,
新建的类可以称为子类或者派生类.
3)继承的例子
class A:
    pass
class B:
    pass
class SubC(A):
    pass
class SubD(A,B):
    pass
print(A.__bases__)  #无指定的父类,继承的是object类,object是C的接口,拥有丰富的特性,也是所有类的基类
print(SubC.__bases__)  #单继承
print(SubD.__bases__) #多继承,类的传入顺序就是继承顺序

# b.多态
# 多态指的是一类事物有多种形态,例如动物:包括了人,猪,狗等等不同的对象
#不同的对象调用相同的方法然后得到不同的结果
import abc
class Animal: #同一类事物:动物
    # @abc.abstractmethod
    def talk(self):
        print(111)

class People(Animal): #动物的形态之一:人
    def talk(self):
        print('say hello')

class Dog(Animal): #动物的形态之二:狗
    def talk(self):
        print('say wangwang')

class Pig(Animal): #动物的形态之三:猪
    def talk(self):
        # super(Pig,self).talk()  #调用父类的方法
        print('say aoao')
a = Pig()
a.talk()
b = Dog()
b.talk()

c.封装
隐藏对象的属性和实现细节,近对外提供公共的访问方式,将变化隔离,提高安全性和复用性.
私有方法例子:
class A:
    def __init__(self):
        self.__x = 10  #变为类私有变量只能让内部方法调用
    def __foo(self):  #私有方法,内部方法调用
        print('x = %s from A' % self.__x)
    def bar(self):  #可以调用内部的私有变量和私有方法,以公共的形式让实例的对象可以间接调用私有内容
        self.__foo()
ret = A()
ret.bar()   
'''
#6.在面向对象中有一些被装饰器装饰的方法,先说说有哪些装饰器,再说说这些装饰器的作用和效果
'''
面向对象的装饰器包含三种:property,classmethod,staticmethod
a.property
一种特殊的属性,访问它时会执行一段功能(函数),然后返回值
可以将类的函数定义为特性,对象再去使用的时候obj.name,根本无法察觉自己的name是执行了一个函数计算出来的,
遵循了统一访问的原则.
一个静态属性property本质就是实现了get,set,delete三种方法
property例子
class Goods:
    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property   #将方法变为特性的装饰器
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter   #只有定义了 property装饰器的方法可以使用setter
    def price(self, value):
        self.original_price = value

    @price.deleter #只有定义了 property装饰器的方法可以使用deleter
    def price(self):
        del self.original_price
obj = Goods()  #实例化成为一个对象
obj.price         # 获取商品价格  利用get的方法
obj.price = 200   # 修改商品原价  利用setter的方法
print(obj.price)  #打折之后的价格
print(obj.original_price) #原价已被改为200
del obj.price     # 删除商品原价  利用deleter的方法
# print(obj.original_price)  #已经获取不到类的这个属性变量了 会报错

#b.classmethod
#classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，
# 可以来调用类的属性，类的方法，实例化对象等。
class Classmethod_Demo():
    role = 'dog'
    @classmethod   
    def func(cls):  #无需调用self 
        print(cls.role)
Classmethod_Demo.func()  #无需实例化直接调用方法

#c.staticmethod
# staticmethod 返回函数的静态方法,该方法不强制要求传递参数
class Staticmethod_Demo():
    role = 'dog'
    @staticmethod
    def func():
        print("当普通方法用")
a = Staticmethod_Demo
a.func()  #可以被实例化的对象当静态字段用
print(a.role)  
Staticmethod_Demo.func() #也可以被类直接当静态字段用
print(Staticmethod_Demo.role)
'''

#7请说明新式类和经典类的区别,至少两个
'''
a.python3中统一都是新式类,默认都是继承object类,pyhon2中才分新式类与经典类,只有(object)之后在可以变为新式类
b.多继承情况下,新式类会按照广度优先的方法寻找方法,经典类会按照深度优先的方法寻找方法
class A(object):
    def test(self):
        print('from A')
class B(A):
    def test(self):
        print('from B')
class C(A):
    def test(self):
        print('from C')
class D(B):
    def test(self):
        print('from D')
class E(C):
    def test(self):
        print('from E')
class F(D,E):
    # def test(self):
    #     print('from F')
    pass
f1=F()
f1.test()
print(F.__mro__) #只有新式才有这个属性可以查看线性列表，经典类没有这个属性

#新式类继承顺序:F->D->B->E->C->A
#经典类继承顺序:F->D->B->A->E->C
'''


#8请说出下面一段代码的输出并解释原因？
'''
class Foo:
    def func(self):
        print('in father')
class Son(Foo):
    def func(self):
          print('in son')
        # super(Son,self).func()  #想调用同名父类的方法
        # Foo.func(self)
# 原因:在继承中,如果父类的方法子类中也有一个同名的,实例化子类的对象只能调用子类的方法
s = Son()
s.func()
s_f = Foo()
s_f.func()
'''
#正则部分的作业
#1.匹配整数或者小数(包括正数和负数)
import re
'''
ret1 = re.findall('-?\d+(?:\.\d+)?','123.45')
print(ret1)
'''
#2.匹配年月日日期 格式 2018-12-6
'''
ret = re.search('\d{4}-([0-1][0-2]|[1-9])-([0-3][0-9]|[0-9])','2018-12-6') #只能匹配正确的日期
print(ret.group())
'''
#3.匹配qq号码
'''
ret = re.search('[1-9]\d{4,10}','391180255')
print(ret.group())
'''
#4.匹配11位的电话号码
'''
ret = re.search('^(13|14|15|18)[0-9]{9}$','18630871234')
print(ret.group())
'''
#5.长度为8-10位的用户密码:包括数字字母下下划线
'''
ret = re.search('\w{8,10}','23434_dsf_23')
print(ret.group())
'''
#6.匹配验证码:4位数字字母组成的
'''
ret = re.search('[0-9a-zA-Z]{4}','23dE')
print(ret.group())
'''
#7匹配邮箱地址
'''
ret = re.search('\w+@\w+\.\w+','linsenquan@btte.net')
print(ret.group())
'''
#8从类似
# <a>wahaha</a>
# <b>banana</b>
# <h1>qqxing</h1>
# 匹配出wahaha banana qqxing内容
# 匹配出a,b,h1这样的内容
'''
ret = re.findall('<\w+>(\w+)','<a>wahaha</a>')
print(ret)
ret1 = re.search('<\w+>(\w+)','<a>wahaha</a>')
print(ret1.group(1))
ret2 = re.search('<(?P<tab>\w+)>(?P<con>\w+)</(?P=tab)>','<h1>qqxing</h1>')
# ret3 = re.findall('<(?P<tab>\w+)>(?P<con>\w+)</(?P=tab)>','<h1>qqxing</h1>')
# print(ret3)
print(ret2.group('tab'))
print(ret2.group('con'))
'''
#9 从'1 - 2 *((60-30 +(-40/5) * (9-2*5/3 + 7/3 *99/4*2998 +10 *568/14)) - (-4*3)/(16-3*2))'
#匹配出最内层括号已经表达式
'''
ret = re.search('\([^()]+\)','1 - 2 *((60-30 +(-40/5) * (9-2*5/3 + 7/3 *99/4*2998 +10 *568/14)) - (-4*3)/(16-3*2))')
print(ret.group())
'''
#10从9-2*5/3 + 7/3 *99/4*2998 +10 *568/14的表达式中从左到右匹配第一个乘法或者除法
'''
ret = re.search('-?[\d\.]+[*/][\d+\.]','9-2*5/3 + 7/3 *99/4*2998 +10 *568/14)')
print(ret.group())
'''
#11匹配一篇英文文章的标题 类似The Voice Of China
'''
ret = re.search('([A-Z][a-z]+\s)+','The Voice Of China ')
print(ret.group())
'''
#12匹配一个网址,类似 https://www.baidu.com

'''
ret = re.search('https?://www\.\w+\.com','https://www.baidu.com')
print(ret.group())
'''
#13匹配年月日日期,类似2018-12-06 2018/12/06 2018.12.06
'''
ret = re.search('\d{4}[-./]([0-1][0-2]|[1-9])[-./]([0-3][0-9]|[0-9])','2018-12-06')
print(ret.group())
ret2 = re.search('\d{4}[-./]([0-1][0-2]|[1-9])[-./]([0-3][0-9]|[0-9])','2018.12.06')
print(ret2.group())
ret2 = re.search('\d{4}[-./]([0-1][0-2]|[1-9])[-./]([0-3][0-9]|[0-9])','2018/12/06')
print(ret2.group())
'''
#14.匹配15位或者18位的身份证号
'''
ret = re.search('^([1-9]\d{16}[0-9x]|[1-9]\d{14})$','330322199310033322')
print(ret.group())
'''
#15.从lianjia.html中匹配出标题,户型和面积,结果如下
# [(' 金台路交通部委楼南北大三居带客厅 单位自持物业 ', '3室 1厅',  '91.22平米 '),
#  ('西山枫林 高楼层南向两居 户型方正 采光好 ', '2室 1厅','94.14平米 ')]
'''
lst = []
com = re.compile('<div class="title">.*?<a .*?>(?P<type>[\w\s]+)</a>.*?<div class="address">.*?<span class="divide">/</span>(?P<type2>\w+)'
                 '<span class="divide">/</span>(?P<type3>\w+\.\w+).*?<span class="divide">',re.S)
def parsePage(s):
    ret = com.finditer(s)
    for i in ret:
        yield  (i.group('type'),i.group('type2'),i.group('type3'))
with open('F:\pywork\Day6linsenquan2018\lianjia.html','r',encoding='utf-8') as f:
        info = f.read()
        # print(info)
        ret = parsePage(info)
        for obj in ret:
            # print(obj)
            lst.append(obj)
print(lst)
'''

