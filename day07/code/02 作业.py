'''
1. 有多个课程，课程要有定价
2. 有多个班级，班级跟课程有关联
3. 有多个学⽣，学⽣报名班级，交这个班级对应的课程的费⽤



4. 有多个⽼师，可以分布在不同校区，上不同班级的课

5. 有多个员⼯，可以分布在不同校区在总部可以统计各校区的账户余额、员⼯⼈数、学员⼈数
6. 学⽣可以转校、退学
'''

class Course:
    def __init__(self, name, price, outline):
        self.name = name
        self.price = price
        self.__outline= outline


class Class:
    def __init__(self, class_num, cour_obj, school_obj): # 学校先不管
        self.class_num = class_num
        self.cour_obj = cour_obj
        self.school_obj = school_obj


class Stu:
    def __init__(self, name, age, degree, class_obj, balance):
        self.name = name
        self.age = age
        self.degree = degree
        self.class_obj= class_obj
        self.balance = balance
        self.class_obj.school_obj.stu_list.append(self)


    def pay(self):
        # 扣钱
        self.balance -= self.class_obj.cour_obj.price
        print("学生交学费")
        # 学校要加钱
        self.class_obj.school_obj.money += self.class_obj.cour_obj.price


class Staff:
    def __init__(self, name, age, position, salary, dept, school_obj):
        # 账户
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.dept = dept
        # 给员工指定学校
        self.school_obj = school_obj
        # self.school_obj.staff_list.append(self)
        self.school_obj.new_staff(self) # 注册新员工


class Teacher(Staff):
    def teaching(self, class_obj):
        print(f"{self.name}在{class_obj.class_num}上课")


class School:
    def __init__(self, name, address, school_obj=None):  # school_obj 上级  北京
        self.name = name
        self.address = address
        self.money = 100000
        # 员工信息
        self.staff_list = [] # 有员工了
        self.head = school_obj #  保存好上级
        self.branches = []  # 分校列表
        self.stu_list = []
        if self.head:
            self.head.branches.append(self)


    def show_money(self):
        return self.money

    def pay_roll(self):
        for staff in self.staff_list:
            self.money -= staff.salary
            print(f"{staff.name}发工资了, 发了{staff.salary}")

    """
    北京
        上海
        深圳
        大兴
    """
    def count_staff_num(self): # 统计员工数量
        totle_num = len(self.staff_list) #  北京 1 上海 2
        print(f"{self.name}有{totle_num}")
        for branch  in self.branches: # 上海
            totle_num += branch.count_staff_num()
        return totle_num

    def count_stu_num(self):
        totle_num = len(self.stu_list)
        print(f"{self.name}有{totle_num}")
        for branch  in self.branches: # 上海
            totle_num += branch.count_stu_num()
        return totle_num

    def new_staff(self, staff):
        self.staff_list.append(staff)


school1 = School("老男孩", "美丽富饶的沙河")
school2 = School("上海分校", "美丽富饶的浦东", )
school3 = School("深圳分校", "美丽富饶的深圳河", )
school4 = School("大兴分校", "美丽富饶的西瓜", )

c1 = Course("python", 60, "神马都没有")
c2 = Course("linux", 6, "神马都没有")
c3 = Course("go", 600, "神马都没有")


class1 = Class("py01", c1, school1)
class2 = Class("py02", c1, school2)
class3 = Class("linux1", c2, school3)
class4 = Class("linux2", c2, school4)
class5 = Class("linux3", c2, school4)

s1 = Stu("李连杰", 18, "本科", class1, 5000)
s2 = Stu("成龙", 18, "本科", class1, 5000)
s3 = Stu("洪金宝", 18, "本科", class1, 5000)
s4 = Stu("元杰", 18, "本科", class1, 5000)

s1.pay()
s2.pay()
s3.pay()
s4.pay()

stf1 = Staff("吴培qi1", 18, "厕所guanliyuan", 100, "车锁i", school1)
stf2 = Staff("吴培qi2", 18, "厕所guanliyuan", 100, "车锁i", school2)
stf3 = Staff("吴培qi3", 18, "厕所guanliyuan", 100, "车锁i", school3)
stf4 = Staff("吴培qi4", 18, "厕所guanliyuan", 100, "车锁i", school4)
stf5 = Staff("吴培qi5", 18, "厕所guanliyuan", 100, "车锁i", school2)
stf6 = Staff("吴培qi6", 18, "厕所guanliyuan", 100, "车锁i", school3)

print(school1.show_money())
school1.pay_roll()
print(school1.show_money())

# #  Staff
t1 = Teacher("alex", 18, "打杂的", 1, "路飞扛把子", )

#
# t1.teaching(class3)
# t1.teaching(class2)
# t1.teaching(class1)
print("一共有%s" % school1.count_staff_num())
