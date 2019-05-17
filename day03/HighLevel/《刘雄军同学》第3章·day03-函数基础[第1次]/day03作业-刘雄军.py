# 3.周末大作业：实现员工信息表
# 文件存储格式如下：
# id，name，age，phone，job
# 1,Alex,22,13651054608,IT
# 2,Egon,23,13304320533,Tearcher
# 3,nezha,25,1333235322,IT
#
# 现在需要对这个员工信息文件进行增删改查。
#
# 不允许一次性将文件中的行都读入内存。
# 基础必做：
# a.可以进行查询，支持三种语法：
# select 列名1，列名2，… where 列名条件
# 支持：大于小于等于，还要支持模糊查找。
# 示例：
# select name, age where age>22
# select * where job=IT
# select * where phone like 133
#
# 进阶选做：
# b.可创建新员工记录，id要顺序增加
# c.可删除指定员工记录，直接输入员工id即可
# d.修改员工信息
# 语法：set 列名=“新的值” where 条件
# #先用where查找对应人的信息，再使用set来修改列名对应的值为“新的值”
#
# 注意：要想操作员工信息表，必须先登录，登陆认证需要用装饰器完成
# 其他需求尽量用函数实现

def my_system():
     welcome ='''
************员工信息查询系统************
     请选择：
            查询请按1
            退出请按2
***************************************
     '''
     print(welcome)

def search():
    formation='''
    1：（按年龄查询）select name, age where age>22
    2：（按职业查询）select * where job=IT
    3：（按电话号码查询）select * where phone like 133
    '''
    print(formation)

    while True:
        search_way = input('请输入您的查询方式(退出请按Q)：')
        res = []
        count = 0
        if search_way.upper() == 'Q':
            exit()
        if search_way =='1':
            age_search = input('请输入要查询的最小年龄：')
            with open(r'E:\linux\python自动化开发培训\作业\info.txt',encoding='utf-8') as f:
                for line in f:
                    each_line = line.split(',')
                    if int(each_line[2]) >= int(age_search):
                        res.append(line)
                        count += 1
            print("查询的结果为：")
            for per in res:
                print(per)
            print('共有%s个员工满足查询信息条件!'%count)
            break
        elif search_way =='2':
            dept_search = input('请输入要查询的职业：')
            with open(r'E:\linux\python自动化开发培训\作业\info.txt',encoding='utf-8') as f:
                for line in f:
                    each_line = line.split(',')
                    if dept_search in line:
                        res.append(line)
                        count += 1
            print("查询的结果为：")
            for per in res:
                print(per)
            print('共有%s个员工满足查询信息条件!'%(count))
            break
        elif search_way =='3':
            phone = input('请输入要查询的电话号码：')
            with open(r'E:\linux\python自动化开发培训\作业\info.txt',encoding='utf-8') as f:
                for line in f:
                    each_line = line.split(',')
                    if phone in line:
                        res.append(line)
                        count += 1
            print("查询的结果为：")
            for per in res:
                print(per)
            print('共有%s个员工满足查询信息条件!' %(count))
            break
        else:
            print('请重新输入！')

my_choice = {
            '1':search,
            '2':'quit'
             }
while True:
    my_system()
    choice = input('请输入数字：')
    if choice not in my_choice:
        print("输入错误，请重新输入！")
        continue
    if int(choice) == 2:
        exit()
    else:
        my_choice[choice]()

