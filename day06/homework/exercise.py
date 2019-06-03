# -----------------------------网站中-----------------------------------------
# 1、简述类、对象、实例化、实例是分别是什么
#   类:为抽象化的模型,主要由属性和方法构成
#   对象:使用类初始化完成后创建的
#   实例化:创建对象的过程叫做实例化
#   实例:实例即对象

# 2、请简述面向对象三大特性？
# 封装、继承、多态
# 封装：将多个属性、方法等内容包裹至一个对象之中
# 继承：子类可以使用父类中的非私有的属性、方法
# 多态：一个参数允许多种形态，鸭子模型

# 3、说说python中所说的封装是什么意思？
# 封装：将多个属性、方法等内容包裹至一个对象之中

# 4、多态是怎么回事？在python中是如何体现的？
# 多态：一个参数允许多种形态，鸭子模型

# 5、说说面向对象中“私有”的概念以及应用
# 私有是以两个下划线开头命名的，不想被外部直接访问的内容

# 6、在面向对象中有一些被装饰器装饰的方法，先说说有哪些装饰器，再说说这些装饰器的作用，以及装饰
# 之后的效果
# classmethod 类方法，可以将普通方法转换为类方法，调用时直接使用类名.方法即可
# staticmethod 静态方法,可以将普通方法转换为静态方法，不需要实例化对象即可使用。
# property 方法转换为属性,使用对象.方法名调用

# 8、请说出上面一段代码的输出并解释原因？


# class Foo:
#     def func(self):
#         print('in father')
#
#
# class Son(Foo):
#     def func(self):
#         print('in son')
#
#
# s = Son()
# s.func()
# 会输出“in son",因为子类中已存在func方法，会先执行子类中存在的方法，不会执行父类中的方法


# -----------------------------大作业-----------------------------------------
# 1. 类、对象、实例、实例化有什么关系 ？
# 类为事物的抽象，或是类型，用来概括对象
# 对象是由类生成的，对象有具体的内容
# 实例即对象
# 实例化即创建对象的过程

# 2. 类属性和实例属性有什么区别？
# 存在空间不同，类属性可通过类名.属性调用，实例属性通过创建的实例.属性调用

# 3. 写个实际使⽤类属性的场景代码
# class Person:
#     country = '唐朝'
#
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#
# person1 = Person('张三', '男')
# person2 = Person('李四', '女')
# print(person1.name, person1.gender, Person.country)
# print(person2.name, person2.gender, Person.country)
# Person.country = '宋朝'  # 共用一个类属性,方便一次性更改
# print(person1.name, person1.gender, Person.country)
# print(person2.name, person2.gender, Person.country)

# 4. ⾃⼰设计场景并写个封装的代码
# class Account:  # 银行帐号
#     def __init__(self, name, passwd, money=0):  # 初始化
#         self.name = name
#         self.passwd = passwd
#         self.money = money
#
#     def get_money(self, name, passwd, money):  # 取钱
#         msg = {'flag': False, 'msg': '', 'money': 0}
#         if money.isdigit():
#             money = int(money)
#             if self.name == name and self.passwd == passwd:
#                 if self.money >= money:
#                     self.money -= money
#                     msg['flag'] = True
#                     msg['msg'] = '取款成功!'
#                     msg['money'] = self.money
#                 else:
#                     msg['msg'] = '余额不足!'
#             else:
#                 msg['msg'] = '帐号或密码不正确!'
#         else:
#             msg['msg'] = '金额格式不正确!'
#         return msg
#
#     def save_money(self, name, money):  # 存钱
#         msg = {'flag': False, 'msg': '', 'money': 0}
#         if self.name == name:
#             if money.isdigit():
#                 money = int(money)
#                 self.money += money
#                 msg['flag'] = True
#                 msg['msg'] = '存款成功!'
#                 msg['money'] = self.money
#             else:
#                 msg['msg'] = '存款失败!金额输入错误!'
#         else:
#             msg['msg'] = '存款失败!帐号错误!'
#         return msg
#
#     def display_money(self, name, passwd):  # 查询
#         msg = {'flag': False, 'msg': '', 'money': 0}
#         if self.name == name and self.passwd == passwd:
#             msg['flag'] = True
#             msg['msg'] = '查询成功!'
#             msg['money'] = self.money
#         else:
#             msg['msg'] = '帐号或密码不正确!'
#         return msg
#
#
# def operate():
#     tom = Account('tom', 'jerry', 100)  # 初始帐号
#
#     # 存钱
#     print('存款'.center(50, '-'))
#     name = input('请输入存款帐号:')
#     money = input('存款金额:')
#     result = tom.save_money(name, money)
#     if result['flag']:
#         print(f'{result["msg"]},您的帐号:{name},存入金额{money},帐号余额:{result["money"]}')
#     else:
#         print(f'{result["msg"]}')
#
#     # 取钱
#     print('取款'.center(50, '-'))
#     name = input('请输入取款帐号:')
#     passwd = input('请输入取款密码:')
#     money = input('取款金额:')
#     result = tom.get_money(name, passwd, money)
#     if result['flag']:
#         print(f'{result["msg"]},您的帐号:{name},取出金额{money},帐号余额:{result["money"]}')
#     else:
#         print(f'{result["msg"]}')
#
#     # 查询
#     print('查询'.center(50, '-'))
#     name = input('请输入查询帐号:')
#     passwd = input('请输入查询密码:')
#     result = tom.display_money(name, passwd)
#     if result['flag']:
#         print(f'{result["msg"]},您的帐号:{name},帐号余额:{result["money"]}')
#     else:
#         print(f'{result["msg"]}')
#
#
# operate()

# 5. ⾃⼰设计场景并写个继承的代码

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(f'{self.name}在吃')
#
#     def move(self):
#         print(f'{self.name}在动')
#
#     def sleep(self):
#         print(f'{self.name}在睡')
#
#
# class Bird(Animal):
#     def __init__(self, name):
#         self.name = name
#
#     def move(self):
#         print(self.name + '在飞')
#
#
# class Cat(Animal):
#     def __init__(self, name):
#         self.name = name
#
#     def move(self):
#         print(self.name + '在跑')
#
#
# kitty = Cat('tom')
# kitty.eat()
# kitty.sleep()
# kitty.move()
#
# chicken = Bird('bibi')
# chicken.eat()
# chicken.sleep()
# chicken.move()

# 6. ⾃⼰设计场景并写个多态的代码
# def func(duck):
#     duck.gaga()
#
#
# class Duck:
#     def gaga(self):
#         print('鸭子嘎嘎')
#
#
# class Goose:
#     def gaga(self):
#         print('鹅嘎嘎')
#
#
# func(Duck())
# func(Goose())

# 7. ⾃⼰设计场景写个类组合的关系 代码，⽐如 cs游戏，⼈是⼀个类， 枪是⼀个类，⼈可以选择不同的枪。

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def shoot(self, gun):
#         print(f'{self.name}选择了{gun.name}')
#         gun.shoot()
#
#
# class Gun:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def shoot(self):
#         print(f'哒哒哒,冒{self.color}火的~')
#
#
# gun1 = Gun('乌瑟', '蓝')
# gun2 = Gun('AK47', '红')
# tom = Person('tom')
# tom.shoot(gun1)
# tom.shoot(gun2)


# 校园管理系统
# 设计⼀个培训机构管理系统，有总部、分校，有学员、⽼师、员⼯，实现具体如下需求：
# 1. 有多个课程，课程要有定价
# 2. 有多个班级，班级跟课程有关联
# 3. 有多个学⽣，学⽣报名班级，交这个班级对应的课程的费⽤
# 4. 有多个⽼师，可以分布在不同校区，上不同班级的课
# 5. 有多个员⼯，可以分布在不同校区在总部可以统计各校区的账户余额、员⼯⼈数、学员⼈数
# 6. 学⽣可以转校、退学
import time


class School:  # 学校
    def __init__(self, name, address, money):
        self.name = name  # 校名
        self.address = address  # 校址
        self.branch_lst = []  # 分校列表
        self.staff_lst = []  # 员工列表
        self.class_lst = []  # 班级列表
        self.__money = money  # 学校存款
        print(f'新建学校:{self.name},地址:{self.address},初始资金:{self.__money}')

    def pay_roll(self):  # 发工资
        for staff in self.staff_lst:
            self.__money -= staff.salary
            print(f'为员工:{staff.name}支付了工资{staff.salary}元')

    def count_staff_num(self):  # 统计员工人数
        staff_num = 0
        for branch in self.branch_lst:
            staff_num += len(branch.staff_lst)
            print(f'{branch.name}学校有员工:{staff_num}名')
        staff_num += len(self.staff_lst)
        print(f'{self.name}有员工:{len(self.staff_lst)}名')
        print(f'所有学校总计员工:{staff_num}名')

    def count_stu_num(self):  # 统计学员人数
        stu_num = 0
        for cls in self.class_lst:
            stu_num += len(cls.stu_lst)
        print(f'{self.name}有学员:{stu_num}名')
        for branch in self.branch_lst:
            branch_stu_num = 0
            for cls in branch.class_lst:
                branch_stu_num += len(cls.stu_lst)
            print(f'{branch.name}有学员:{branch_stu_num}名')
            stu_num += branch_stu_num
        print(f'总计学员:{stu_num}名')

    def new_staff_enrollment(self, staff):  # 新员工注册
        self.staff_lst.append(staff)
        print(f'{self.name}新加入员工:{staff.name},职位:{staff.position}')

    def new_class(self, new_cls):  # 新班级
        self.class_lst.append(new_cls)
        print(f'{self.name}新加入班级:{new_cls.class_num}')

    def get_tuition(self, money):  # 收费
        self.__money += money
        print(f"{self.name}收到学费{money}元")

    def display_money(self):  # 显示余额
        money = 0
        for branch in self.branch_lst:
            money += branch.__money
            print(f'{branch.name}有余额:{branch.__money}')
        money += self.__money
        print(f'{self.name}有余额:{self.__money}元')
        print(f'总计余额:{money}元')


class BranchSchool(School):  # 分校
    def __init__(self, name, address, headquater, money):
        super(BranchSchool, self).__init__(name, address, money)
        self.__headquater = headquater  # 所属上级校区对象
        self.__headquater.branch_lst.append(self)  # 加入到总校列表


class Course:  # 课程
    def __init__(self, name, price, outline):
        self.name = name
        self.price = price
        self.__outline = outline
        self.course_class_lst = []
        print(f'新课程{self.name},价格:{self.price}')


class Staff:  # 职员
    def __init__(self, name, age, position, salary, dept, school):
        self.name = name
        self.age = age
        self.position = position  # 职位
        self.salary = salary  # 薪水
        self.dept = dept  # 部门
        self.school = school  # 所在校区对象
        self.school.new_staff_enrollment(self)  # 加入学校

    def operation1(self, *args):
        return type(args)

    def operation2(self, *args):
        pass

    def operation3(self):
        pass


class Class(BranchSchool, Course):  # 班级
    def __init__(self, class_num, course_obj, school_obj):
        self.class_num = class_num  # 学期
        self.course_obj = course_obj  # 课程对象
        self.school_obj = school_obj  # 所属校区
        self.stu_lst = []  # 学生列表
        self.class_record = []  # 上课记录
        self.school_obj.new_class(self)  # 班级加入至学校
        self.course_obj.course_class_lst.append(self)  # 班级加入至课程列表

    def create_teaching_record(self, record):  # 创建上课记录
        self.class_record.append(record)
        print(record)

    def drop_out(self, student_obj):  # 退学
        self.stu_lst.remove(student_obj)  # 班级列表中删除
        print(f'{student_obj.name}退学了!')


class Teach(Staff, Class):  # 讲师
    def teaching(self, course_obj, class_obj):  # 讲课
        record = f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())},{self.name}," \
            f"在{class_obj.class_num}班,讲{course_obj.name}课"
        class_obj.create_teaching_record(record)


class Student(Class):  # 学员
    def __init__(self, name, age, degree, class_obj, balance):
        self.name = name
        self.age = age
        self.degree = degree  # 学位
        self.class_obj = class_obj  # 报名班级
        self.balance = balance  # 余额
        self.class_obj.stu_lst.append(self)

    def pay_tuition(self):  # 交学费
        money = self.class_obj.course_obj.price  # 获取价格
        self.balance -= money  # 学生减钱
        record = f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())},{self.name}," \
            f"交{self.class_obj.course_obj.name}课学费,{money}元"
        print(record)
        self.class_obj.school_obj.get_tuition(money)  # 学校收钱

    def change_school(self, new_cls):  # 转学
        self.class_obj.stu_lst.remove(self)
        new_cls.stu_lst.append(self)
        print(f'{self.name}由{self.class_obj.class_num}转到了{new_cls.class_num}')


def main():
    print("新建学校".center(50, '-'))
    school = School('新东方总部', '北京', 10000)
    branch_school = BranchSchool('新东方天津', '天津', school, 5000)
    print("新建课程".center(50, '-'))
    # 1. 有多个课程，课程要有定价
    english_course = Course('英语初级', 80, {'第一阶段': ['介绍', '初级英语'], '第二阶段': ['中级英语', '高级英语']})
    high_course = Course('英语高级', 70, {'第一阶段': ['介绍', '初级数学'], '第二阶段': ['中级数学', '高级数学']})
    # 2. 有多个班级，班级跟课程有关联
    print("新建班级".center(50, '-'))
    english_class1 = Class("英语初级1班", english_course, school)
    english_class2 = Class('英语初级2班', english_course, school)
    high_class1 = Class('英语高级1班', high_course, branch_school)
    high_class2 = Class('英语高级2班', high_course, branch_school)
    # 3. 有多个学⽣，学⽣报名班级，交这个班级对应的课程的费⽤
    print("新建学生".center(50, '-'))
    stu1 = Student('刘一', 20, '初中', english_class1, 200)
    stu1.pay_tuition()
    stu2 = Student('陈二', 30, '高中', english_class2, 300)
    stu2.pay_tuition()
    stu3 = Student('张三', 40, '大学', english_class2, 400)
    stu3.pay_tuition()

    stu4 = Student('李四', 20, '初中', high_class1, 200)
    stu4.pay_tuition()
    stu5 = Student('王五', 30, '高中', high_class2, 300)
    stu5.pay_tuition()
    stu6 = Student('赵六', 40, '大学', high_class2, 400)
    stu6.pay_tuition()
    # 4. 有多个⽼师，可以分布在不同校区，上不同班级的课
    print("新建老师".center(50, '-'))
    teacher1 = Teach('王老师', 50, '高级', 200, '总经办', school)
    teacher2 = Teach('李老师', 50, '高级', 100, '总经办', school)
    teacher3 = Teach('张天老师', 50, '高级', 150, '总经办', branch_school)
    teacher4 = Teach('孙老师', 50, '高级', 220, '总经办', branch_school)

    # 5. 有多个员⼯，可以分布在不同校区在总部可以统计各校区的账户余额、员⼯⼈数、学员⼈数
    print("新建员工".center(50, '-'))
    staff1 = Staff('王强', 20, '经理', 50, '财务', school)
    staff2 = Staff('李丁', 30, '员工', 20, '财务', branch_school)
    print("查询各校区余额".center(50, '-'))
    school.display_money()  # 获取各校区余额
    print("查询各校区员工".center(50, '-'))
    school.count_staff_num()  # 获取员工人员
    print("查询各校区学员".center(50, '-'))
    school.count_stu_num()  # 获取学员人数

    # 6. 学⽣可以转校、退学
    print("学员退学".center(50, '-'))
    english_class1.drop_out(stu1)
    print("学员转校".center(50, '-'))
    stu2.change_school(high_class1)


if __name__ == '__main__':
    main()
