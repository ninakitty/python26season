import pickle
import os
Base_Dir = os.path.dirname(os.path.abspath(__file__))
userinfo = os.path.join(Base_Dir,'userinfo.txt')  #存用户名密码类别
courseinfo = os.path.join(Base_Dir,'courseinfo.pickle')  #存所有的课程类的对象
studentinfo = os.path.join(Base_Dir,'studentinfo.pickle') #存学生类(带courses属性)的对象
studentname = os.path.join(Base_Dir,'studentname.pickle') #存学生类的对象

class Person(object):  #父类
    def quit(self):
        exit('退出成功')
    def show_all_course(self):
         course_obj = self.read_file(courseinfo,'rb',True)  #从文件中load对象的生成器
         for k,v in enumerate(course_obj,1):  #for循环调用生成器
             print('''%s.课程名字:%s 价格:%s元 周期:%s ''' %(k,v.course_name,v.course_price,v.course_period))
    def write_file(self,filepath,mode_type,obj=None): #序列化写入对象
        with open(filepath,mode_type) as f:
            pickle.dump(obj,f)
            f.flush()  #刷新文件存储
    def read_file(self,filepath,mode_type,obj=None): #序列化读出对象
        if obj:
            with open(filepath,mode_type) as f:
                while 1:
                    try:
                        yield pickle.load(f) #取对象只能每次直接pickle文件
                    except EOFError:
                        break

class Course: #定义一个课程类
    def __init__(self,name,price,period):
        self.course_name = name
        self.course_price = price
        self.course_period = period

class Student(Person):  #继承父类的方法
    def __init__(self,name):
        self.name = name
        self.course = []
    def select_course(self):
        self.show_all_course()
        course_obj = self.read_file(courseinfo, 'rb', True)
        # while 1:
        # cmd = input('请输入你要选择的课程名字:或者q退出选课')
        #     if cmd =='q':
        #         break
        cmd = input('请输入你要选择的课程名字:')
        for i in course_obj:
            if cmd == i.course_name:   #判断输入的课程名字与对象的课程属性是否相等
                self.course.append(i.course_name)
        # print(self.course)
        student_obj = Student(self.name)  #实例化Student拿到对象
        student_obj.course = self.course   #对象的属性重新赋值
        if self.write_file(studentinfo,'ab',student_obj):  #带有新属性的学生类序列化到文件中
            print('[%s:%s] 选课成功\n' % ('Student', self.name))

    def show_select_course(self):
        select_course_obj = self.read_file(studentinfo,'rb',True)
        for i in select_course_obj:
            if i.name == self.name:
                print(''' %s选了%s课程''' % (i.name,''.join(i.course)))

class Manager(Person):  #定义一个管理员类 继承父类使用父类的方法
    def __init__(self,name):
        self.name = name
    def create_student(self):  #创建学生
        user = input('输入学生用户名:').strip()
        pwd = input('输入学生的密码:').strip()
        with open(userinfo,'a',encoding='UTF-8') as f:
            f.write('%s|%s|%s\n' % (user,pwd,'Student'))
        student_obj = Student(user)
        if self.write_file(studentname,'ab',student_obj):  #将学生类序列化到文件中
            print('[%s:%s] 创建成功\n' % ('Student', user))
    def create_course(self):  #创建课程
        course_name = input('course name:').strip()
        course_price = input('course price:').strip()
        course_period = input('course period:').strip()
        course_obj = Course(course_name,course_price,course_period)
        if self.write_file(courseinfo,'ab',course_obj):
            print('创建课程成功:%s' % course_name)
    def show_all_student(self):
        student_obj = self.read_file(studentname,'rb',True)
        for i in student_obj:
            print('学生姓名:%s' % i.name)
    def show_all_student_course(self):
        print('查看所有的学生所选择的课程')
        select_course_obj = self.read_file(studentinfo, 'rb', True)
        for i in select_course_obj:
            print('%s选择了%s课程' % (i.name,''.join(i.course)))

def login():
    try_count = 0
    while try_count<3:  #三次验证登陆
        username = input('请输入用户名:')
        password = input('请输入密码:')
        with open(userinfo,'r') as f:
            for info in f:
                info = info.strip().split('|')
                user,pwd,identity = info[0],info[1],info[2]
                if username == user and password == pwd :
                    print('%s用户%s登陆成功' % (identity,username))
                    return {'username':username,'identity':identity}
                elif  username == user and password == pwd:
                    print('%s用户%s登陆成功' % (identity,username))
                    return {'username': username, 'identity': identity}
            else:
                try_count += 1
                print('你还有%s次机会' % (3 - try_count))

def main():
    ret = login()
    if ret:  #通过身份的标志位判断程序走学生视图还是管理员试图
        if ret['identity'] == 'Student':
            lst_student = ['查看所有课程','选择课程','查看所选课程','退出程序']
            student = Student(ret['username']) #实例化Student类
            while 1:
                for k,v in enumerate(lst_student,1):
                    print(k,v)
                cmd = int(input('请输入选择的数字:').strip())
                if cmd ==1:
                    student.show_all_course()
                elif cmd ==2:
                    student.select_course()
                elif cmd ==3:
                    student.show_select_course()
                elif cmd ==4:
                    student.quit()
                else:
                    print('请输入正确的数字')

        elif ret['identity'] == 'Manager':
            lst_manager = ['创建课程','创建学生账号','查看所有课程','查看所有学生','查看所有学生的选课情况','退出程序']
            manager = Manager(ret['username']) #实例化管理员类
            while 1:
                for k,v in enumerate(lst_manager,1):
                    print(k,v)
                cmd = int(input('请输入选择的数字:').strip())
                if cmd ==1:
                    manager.create_course()
                elif cmd ==2:
                    manager.create_student()
                elif cmd ==3:
                    manager.show_all_course()
                elif cmd ==4:
                    manager.show_all_student()
                elif cmd ==5:
                    manager.show_all_student_course()
                elif cmd ==6:
                    manager.quit()
                else:
                    print('请输入正确的数字')

    else:
        print('登陆失败!')

if __name__ == '__main__':
    main()

