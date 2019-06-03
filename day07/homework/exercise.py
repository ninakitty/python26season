# 练习题:
# 1、new方法和init方法执行的执行顺序
# class Person:
#     def __new__(cls, *args, **kwargs):
#         print('我是new')
#         return object.__new__(cls)
#
#     def __init__(self):
#         print('init')
#
#
# p = Person()
# 先执行new方法然后再执行init方法


# 2、call方法在什么时候被调用
# class Person:
#     def __call__(self, *args, **kwargs):
#         print('我是call方法')
#
#
# p = Person()
# p()
# call方法在对象调用的时间被调用


# 3、请用写一个类，用反射为这个类添加一个静态属性
# class Person:
#     pass
#
#
# setattr(Person, 'name', 'tom')
# print(Person.name)


# 4、请用反射为上题的类的对象添加一个属性name,值为你的名字
# class Person:
#     pass
#
#
# setattr(Person, 'name', 'tom')
# print(Person.name)
# p = Person()
# p.__setattr__('name', 'jerry')
# print(p.name)


# 5、请使用new方法实现一个单例模式
# class Singleton:
#     __single = None
#
#     def __new__(cls, *args, **kwargs):
#         # print('__new__')
#         if not cls.__single:
#             cls.__single = object.__new__(cls)
#         return cls.__single
#
#     def __init__(self):
#         print('__init__')
#
#
# c1 = Singleton()
# c2 = Singleton()
# c3 = Singleton()
# print(id(c1), id(c2), id(c3))
# 6、校验两个文件的一致性
# import hashlib
#
#
# def get_md5(file1, file2):
#     '''
#     比较两个文件是否一致
#     :param file1: 文件1
#     :param file2: 文件2
#     :return: 是否一致
#     '''
#     flag = False
#     with open(file1, mode='rb') as fp1, open(file2, mode='rb')as fp2:
#         obj1 = hashlib.md5()
#         obj1.update(fp1.read())
#         obj2 = hashlib.md5()
#         obj2.update(fp2.read())
#         if obj1.hexdigest() == obj2.hexdigest():  # 比较md5数值
#             flag = True
#     return flag
#
#
# if get_md5('file_a.txt', 'file_b.txt'):
#     print('两个文件一致!')
# else:
#     print('两个文件不一致!')

# 7、加盐的密文登陆
# import hashlib
#
# uname = 'tom'
# passwd = 'd7072cc16da675e4044c8a5ba19ca289'  # 'jerry'
#
# username = input('请输入用户名:')
# password = input('请输入密码:')
# obj = hashlib.md5(b'insert_char')  # 加盐
# obj.update(password.encode('utf8'))
# if username == uname and passwd == obj.hexdigest():
#     print('登录成功!')
# else:
#     print('登录失败!')
# 8、完成一个既可以向文件输出又可以向屏幕输出的日志设置
# import logging
#
# # 格式化
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s: %(message)s')
# # 分别创建file handler和stream handler
# file_handler = logging.FileHandler('x1.txt', 'a', encoding='utf-8')
# stream_handler = logging.StreamHandler()
# # 分别设置显示等级
# file_handler.setLevel(logging.ERROR)
# stream_handler.setLevel(logging.DEBUG)
# # 分别设置格式化
# file_handler.setFormatter(formatter)
# stream_handler.setFormatter(formatter)
#
# # 创建logger
# logger = logging.Logger('tom')
# # 将两个handler添加到logger中
# logger.addHandler(stream_handler)
# logger.addHandler(file_handler)
#
# # 添加告警信息
# logger.critical("报错了")  # 最高级别   50
# logger.error("报错了")  # 40
# logger.warning("警告")  # 30 警告
# logger.info("信息")  # 20 正常信息
# logger.debug("调错")  # 10
# logger.log(9999, "地球炸了")


# 校园管理系统（02）
# 从“学生选课系统” 这几个字就可以看出来，我们最核心的功能其实只有 选课。
# 角色：
#     学生、管理员
# 功能：
#     登陆 ： 管理员和学生都可以登陆，且登陆之后可以自动区分身份
#     选课 ： 学生可以自由的为自己选择课程
#     创建用户 ： 选课系统是面向本校学生的，因此所有的用户都应该由管理员完成
#     查看选课情况 ：每个学生可以查看自己的选课情况，而管理员应该可以查看所有学生的信息
# 工作流程：
#     登陆 ：用户输入用户名和密码
#     判断身份 ：在登陆成果的时候应该可以直接判断出用户的身份 是学生、讲师还是管理员
#     学生用户 ：对于学生用户来说，登陆的工作几乎不变
#         1、查看所有课程
#         2、选择课程
#         3、查看所选课程
#         4、退出程序
#     管理员用户：管理员用户也可以做更多的事情#
#         1、创建课程
#         2、创建学生学生账号
#         3、查看所有课程
#         4、查看所有学生
#         5、查看所有学生的选课情况
#         6、创建讲师
#         7、为讲师指定班级
#         8、创建班级
#         9、为学生指定班级
#         10、退出程序#
#     讲师用户 ：对于讲师用户来说，可以完成的功能如下
#         1、查看所有课程
#         2、查看所教班级
#         3、查看班级中的学生
#         4、退出程序
import hashlib
import os
import traceback
import pickle


class MyMD5:
    @staticmethod
    def get_md5(args, insert_word=''):
        """
        MD5加密
        :param args: 加密文件或字符
        :param insert_word: 加盐字符
        :return:
        """
        obj = hashlib.md5(insert_word.encode('utf8'))
        if os.path.isfile(args):  # 判断是否为文件
            with open(args, mode='rb') as fp:
                obj.update(fp.read())
        elif isinstance(args, str):  # 判断是否为字符
            obj.update(args.encode('utf8'))
        return obj.hexdigest()


class School:
    def __init__(self, name):
        self.name = name  # 校名
        self.person_list = []  # 人员列表
        self.course_list = []  # 课程列表
        self.class_list = []  # 班级列表

    def add_person_list(self, obj):  # 添加人员
        # dic = {'name': obj.name, 'password': obj.password,
        #        'identity': obj.identity, 'school_obj': obj.school_obj}
        self.person_list.append(obj)

    def add_course_list(self, obj):  # 添加课程
        self.course_list.append(obj)

    def add_class_list(self, obj):  # 添加班级
        self.class_list.append(obj)


class Course:  # 课程
    def __init__(self, name, period, outline, school_obj):
        self.name = name  # 课程名称
        self.period = period  # 课时
        self.outline = outline  # 大纲
        self.school_obj = school_obj
        self.school_obj.add_course_list(self)


class Class:
    def __init__(self, name, school_obj):
        self.name = name  # 班级名称
        self.school_obj = school_obj
        self.student_list = []  # 班级学生列表
        self.teacher_list = []  # 班级老师
        self.school_obj.add_class_list(self)

    def get_student_list(self):  # 获取学生列表
        return self.student_list

    def get_teacher_list(self):  # 获取老师列表
        return self.teacher_list


class Person:  # 人员
    def __init__(self, name, password, identity, school_obj, id_num=0):
        self.name = name  # 用户名称
        self.password = MyMD5.get_md5(password)
        self.identity = identity  # 用户身份
        self.id_num = id_num
        self.school_obj = school_obj
        self.school_obj.add_person_list(self)  # 将用户添加到school

    @staticmethod
    def login(username, password, person_list):  # 登录方法
        flag = {'user': '', 'success': False, 'identity': '', 'msg': '登录失败,用户名或密码错误!', 'obj': None}
        for person in person_list:
            if person.name == username and MyMD5.get_md5(password) == person.password:
                flag['success'] = True
                flag['identity'] = person.identity
                flag['user'] = person.name
                flag['msg'] = '登录成功,欢迎光临!'
                flag['obj'] = person
        return flag

    def view_course(self):  # 查看所有课程
        print('查看所有课程'.center(50, '-'))
        for index, course in enumerate(self.school_obj.course_list, 1):
            print(index, course.name)

    @staticmethod
    def logout():  # 登出
        print('退出完成!')
        return 'exit'


class Student(Person):  # 学生
    def __init__(self, name, password, school_obj, id_num=0, class_obj=None, identity='student'):
        super(Student, self).__init__(name, password, identity, school_obj, id_num)
        self.choose_course_list = []  # 所选课程列表
        self.class_obj = class_obj  # 所属班级
        if class_obj:
            self.class_obj.student_list.append(self)

    def student_insert_class(self, class_obj):  # 加入班级
        self.class_obj = class_obj
        self.class_obj.student_list.append(self)

    def choose_course(self):  # 学生选课
        print('学生选课'.center(50, '-'))
        self.view_course()
        course = input('请输入课程序号:')
        if course.isdigit():
            course = int(course)
            if 0 < course <= len(self.school_obj.course_list):
                course_obj = self.school_obj.course_list[course - 1]
                if course_obj in self.choose_course_list:
                    print('此课程已被选择!请不要重复选择!')
                else:
                    self.choose_course_list.append(course_obj)
                    print(f'你选择的课程:{course_obj.name}')
            else:
                print('输入序号错误!')

    def view_choose_course(self):  # 查看所选课程
        print('查看所选课程'.center(30, '-'))
        if len(self.choose_course_list):  # 是否存在课程
            for course in self.choose_course_list:
                print(self.name, '选择了:', course.name)
        else:
            print(self.name, '未选择课程')


class Teacher(Person):
    def __init__(self, name, password, school_obj, id_num=0, class_obj=None, identity='teacher'):
        super(Teacher, self).__init__(name, password, identity, school_obj, id_num)
        self.class_obj = class_obj  # 所教班级
        if class_obj:
            self.class_obj.teacher_list.append(self)

    def view_class(self):  # 查看所教班级
        if self.class_obj:
            print('查看所教班级'.center(50, '-'))
            print('所教班级:', self.class_obj.name)
        else:
            print('---老师未指定班级---')

    def view_class_student(self):  # 查看班级中的学生
        if self.class_obj:
            print('查看班级中的学生'.center(50, '-'))
            for index, student in enumerate(self.class_obj.student_list, 1):
                print(index, student.name)
        else:
            print('---老师未指定班级---')


class Root(Person):  # 管理员
    def create_course(self):  # 创建课程
        print('创建课程'.center(50, '-'))
        name = input('请输入课程名称:')
        period = input('请输入课时:')
        outline = input('请输入大纲:')
        flag = True  # 课程是否存在
        for course in self.school_obj.course_list:
            if course.name == name:
                flag = False
                print('您输入的课程已存在!')
        if flag:
            Course(name, period, outline, self.school_obj)
            print(f'创建课程完成,名称:{name},课时:{period},大纲:{outline}')

    def create_student(self):  # 创建学生账号
        print('创建学生账号'.center(50, '-'))
        name = input('请输入用户名:')
        password = input('请输入密码:')
        if name == '' or password == '':
            print('姓名或密码不能为空!')
        else:
            id_num = len(self.school_obj.person_list)
            Student(name, password, self.school_obj, id_num)
            print(f'学生建立完成,姓名:{name},学号:{id_num}')

    def view_students(self):  # 查看所有学生
        print('查看所有学生'.center(50, '-'))
        for person in self.school_obj.person_list:
            if isinstance(person, Student):
                print(f'姓名:{person.name},编号:{person.id_num}')

    def view_students_course(self):  # 查看所有学生的选课情况
        print('查看所有学生的选课情况'.center(50, '-'))
        for person in self.school_obj.person_list:
            if isinstance(person, Student):  # 筛选出学生
                person.view_choose_course()

    def create_teacher(self):  # 创建老师
        print('创建老师'.center(50, '-'))
        name = input('请输入用户名:')
        password = input('请输入密码:')
        if name == '' or password == '':
            print('姓名或密码不能为空!')
        else:
            id_num = len(self.school_obj.person_list)
            Teacher(name, password, self.school_obj, id_num)
            print(f'老师建立完成,姓名:{name},学号:{id_num}')

    @staticmethod
    def type_choose_help(type_name, class_type, type_list):  # 协助完成类型选择
        """
        协助完成类型选择
        :param type_name: 字符类型的名字
        :param class_type: 需要选择的类
        :param type_list: 需要选择的列表
        :return: 返回选择的内容
        """
        type_index_list = []  # 序号列表
        type_obj = None
        for index, ty in enumerate(type_list):  # 迭代并打印出相应类型数据
            if isinstance(ty, class_type):
                type_index_list.append(index)
                print(f'{type_name}信息,序号:{index + 1},{type_name}名:{ty.name}')
        type_index = input(f'请输入{type_name}序号:')
        if type_index.isdigit():
            type_index = int(type_index) - 1
            flag = True
            for ty_index in type_index_list:
                if type_index == ty_index:
                    type_obj = type_list[type_index]
                    flag = False
            if flag:
                print('序号输入错误!')
        else:
            print('序号输入错误!')

        return type_obj

    def teacher_choose_class(self):  # 为老师指定班级
        print('为老师指定班级'.center(50, '-'))
        teacher = self.type_choose_help('老师', Teacher, self.school_obj.person_list)
        class_obj = self.type_choose_help('班级', Class, self.school_obj.class_list)
        if teacher and class_obj:
            teacher.class_obj = class_obj  # 为老师指定
            class_obj.teacher_list.append(teacher)  # 在班级中加入老师
            print(f'{teacher.name}老师加入到{class_obj.name}班')

    def create_class(self):  # 创建班级
        print('创建班级'.center(50, '-'))
        name = input('请输入班级名:')
        flag = True
        for class_obj in self.school_obj.class_list:
            if class_obj.name == name:  # 班级名称不能重复
                print('班级已存在,请不要重复建立!')
                flag = False
        if flag:
            Class(name, self.school_obj)
            print(f'班级建立完成,班级名:{name}')

    def student_choose_class(self):  # 为学生指定班级
        print('为学生指定班级'.center(50, '-'))
        student = self.type_choose_help('学生', Student, self.school_obj.person_list)
        class_obj = self.type_choose_help('班级', Class, self.school_obj.class_list)
        if student and class_obj:
            if student in class_obj.student_list:
                print(f'学生{student.name}已经加入过此班级,请不要重复操作!')
            else:
                student.class_obj = class_obj  # 学生指定班级
                class_obj.student_list.append(student)  # 班级中添加学生
                print(f'{student.name}学生加入到{class_obj.name}班')


def get_method(_class, method):  # 反射方法
    gn = method
    msg = ''  # 接收返回值
    if hasattr(_class, gn):  # 是否有这个属性
        fn = getattr(_class, gn)  # 获取这个属性
        if callable(fn):  # 是否可被调用
            try:
                msg = fn()
            except Exception:
                print(traceback.format_exc())
        else:
            print(fn)
    else:
        print('没有这个属性')
    return msg


def opera_method_list(person, method_list):  # 处理功能列表
    """
    处理功能列表
    :param person: 人员对象
    :param method_list: 功能列表
    :return:方法执行后的内容
    """
    msg = ''  # 接收返回值
    for index, method in enumerate(method_list):
        print(f'{index + 1},{method[1]}')
    input_num = input('请输入功能序号:')
    if input_num.isdigit():
        input_num = int(input_num)
        if 0 < input_num <= len(method_list):
            msg = get_method(person, method_list[input_num - 1][0])
        else:
            print('输入错误!')
    else:
        print('输入错误!')
    return msg


def do_method(result):  # 执行方法
    """
    从功能列表中选择执行方法
    :param result: 登录成功后返回的结果
    :return: 执行相应方法后的结果
    """
    person = result.get('obj')
    msg = ''
    print('可执行以下功能'.center(50, '*'))
    if isinstance(person, Root):
        method_list = [['view_course', '查看所有课程'], ['create_course', '创建课程'],
                       ['create_student', '创建学生账号'], ['view_students', '查看所有学生'],
                       ['view_students_course', '查看所有学生的选课情况'],
                       ['create_teacher', '创建老师'], ['teacher_choose_class', '为老师指定班级'],
                       ['create_class', '创建班级'], ['student_choose_class', '为学生指定班级'], ['logout', '退出']]
        msg = opera_method_list(person, method_list)
    elif isinstance(person, Student):
        method_list = [['view_course', '查看所有课程'], ['choose_course', '选择课程'],
                       ['view_choose_course', '查看所选课程'], ['logout', '退出']]
        msg = opera_method_list(person, method_list)
    elif isinstance(person, Teacher):
        method_list = [['view_course', '查看所有课程'], ['view_class', '查看所教班级'],
                       ['view_class_student', '查看班级中的学生'], ['logout', '退出']]
        msg = opera_method_list(person, method_list)
    return msg


def main():  # 主方法
    # 准备初始数据
    file = 'database.db'
    if os.path.isfile(file):
        with open(file, mode='rb') as fp:
            school = pickle.load(fp)
    else:
        with open(file, mode='wb') as fp:
            school = School('中国大学')
            Course('英语', 20, {}, school)
            Class('一班', school)
            Root('root', 'root', 'root', school, 1)  # 添加管理员
            Teacher('t1', 't1', school, 2)  # 老师
            Teacher('t2', 't2', school, 3)
            Student('s1', 's1', school, 4)  # 学生
            Student('s2', 's2', school, 5)
            pickle.dump(school, fp)
    # 程序开始
    is_login = False  # 是否登录
    switch = True  # 总开关
    result = ''  # 返回的结果
    # result = {'user': '', 'success': False, 'identity': '', 'msg': '登录失败,用户名或密码错误!'}
    print('''
        欢迎使用选课系统!
        ''')
    while switch:
        # 登录
        if not is_login:
            print('''
                输入1登录,
                输入Q退出
                ''')
            input_char = input('请输入:')
            if input_char.isdigit():
                if input_char == '1':
                    username = input("请输入用户名:")
                    password = input("请输入密码:")
                    result = Person.login(username, password, school.person_list)
                    if result.get('success'):
                        is_login = True
                        print(f'{result.get("msg")}, {result.get("user")},您的身份为:{result.get("identity")}')
                        msg = do_method(result)
                        print()
                        if msg == 'exit':
                            is_login = False
                    else:
                        print(f'{result.get("msg")}')
                else:
                    print('序号输入错误!')
            elif input_char.upper() == 'Q':
                switch = False
            else:
                print('输入错误 !')
        else:
            msg = do_method(result)
            if msg == 'exit':  # 返回值为exit,退出登录
                is_login = False
    # 保存数据
    with open(file, mode='wb') as fp:
        pickle.dump(school, fp)


if __name__ == '__main__':
    main()
