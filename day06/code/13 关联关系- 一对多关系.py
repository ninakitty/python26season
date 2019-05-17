class Teacher:
    def __init__(self, name, stuList = []):
        self.name = name
        self.stuList = stuList

    def teach(self):
        print(f"{self.name}在上课")
        # 所有的学生学习
        for stu in self.stuList:
            stu.study()

class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"{self.name}在学习")






t = Teacher("Sylar")

s1 = Student("蔡徐坤")
s2 = Student("王麻子")
s3 = Student("曾轶可")
s4 = Student("苏醒")

lst = [s1,s2,s3,s4]
#  把列表给老师
t.stuList = lst

t.teach()


# 你 -> 订单
# 订单 -> 商品
# 领导和员工
# 百度 -> 子页面

# 学生 <-> 老师

