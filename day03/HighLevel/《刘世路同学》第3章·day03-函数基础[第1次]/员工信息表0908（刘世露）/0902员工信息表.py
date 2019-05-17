'''
3.周末大作业：实现员工信息表
文件存储格式如下：
id，name，age，phone，job
1,Alex,22,13651054608,IT
2,Egon,23,13304320533,Tearcher
3,nezha,25,1333235322,IT
现在需要对这个员工信息文件进行增删改查。
不允许一次性将文件中的行都读入内存。
基础必做：
a.可以进行查询，支持三种语法：
select 列名1，列名2，… where 列名条件
支持：大于小于等于，还要支持模糊查找。
示例：
select name, age where age>22
select * where job=IT
select * where phone like 133
进阶选做：
b.可创建新员工记录，id要顺序增加
c.可删除指定员工记录，直接输入员工id即可
d.修改员工信息
语法：set 列名=“新的值” where 条件
#先用where查找对应人的信息，再使用set来修改列名对应的值为“新的值”
注意：要想操作员工信息表，必须先登录，登陆认证需要用装饰器完成
其他需求尽量用函数实现
作业要求：需要交整理的函数相关的思维导图
整理的函数知识点的博客
装饰器作业加注释
3.大作业放在3文件夹中
　　文件夹中需要包括：
　　代码
　　流程图（请上交一张png图片。如果没有合适的画图软件，可以用processon画）
　　readme文件（请上交一个txt文件，对作业进行一些简单说明，包括作业的整体思路，如何运行，实现了哪些功能，遇到了哪些问题等。）
'''

#登录验证函数
#操作语句识别函数

def txt_switch(txt):#文件提取文本后，转换成列表
    f = open(txt,mode='r',encoding='utf-8')
    f_list = []#将文本都每一行存储此列表中
    list_dic = []#将列名和明细组合成字典，然后存储在此列表中
    for line in f:
        f_list.append(line.strip().split(','))
    list_name = f_list.pop(0)#取出列名，将列名和明细进行分离
    for i in f_list:
        list_dic.append(dict(zip(list_name,i)))#将列名和明细组合成字典，然后生成列表
    return list_dic#返回一个处理后的列表
    f.close()


def login(username,password):#登陆账号密码验证函数
    account_list = txt_switch('account_info')#调用文本转换函数
    for dic in account_list:
        if username == dic['username'] and password == dic['password']:
            return True
        else:
            return False

def statement_parsing(select):#查询语句解析
    list1 = select.strip().split('where')
    list2 = list1[0].strip().split('select')
    list2.pop(0)
    select_dic = {}
    select_dic['select'] = list2[0].replace(' ','').split(',')
    if '>' in list1[1]:
        select_dic['where'] = list1[1].strip().partition('>')
    elif '<' in list1[1]:
        select_dic['where'] = list1[1].strip().partition('<')
    elif 'like' in list1[1]:
        select_dic['where'] = list1[1].strip().split()#like模糊查询的话，利用空格对查询条件进行分片
    else:
        select_dic['where'] = list1[1].strip().partition('=')
    return select_dic

def statement_run(select):#语句执行函数
    staff_info = txt_switch('staff_info')#调用文件提取函数，将员工信息转换成列表
    select_dic = statement_parsing(select)#调用查询语句解析函数，将语句转换成字典
    select_staff_info = []#将查询到匹配条件的员工信息，存储在列表中
    if '>' in select_dic['where']:
        for staff_item in staff_info:
            if int(staff_item[select_dic['where'][0]]) > int(select_dic['where'][2]):
                select_staff_info.append(staff_item)
    elif '<' in select_dic['where']:
        for staff_item in staff_info:
            if int(staff_item[select_dic['where'][0]]) < int(select_dic['where'][2]):
                select_staff_info.append(staff_item)
    elif '=' in select_dic['where']:
        for staff_item in staff_info:
            if staff_item[select_dic['where'][0]] == select_dic['where'][2]:
                select_staff_info.append(staff_item)
    elif 'like' in select_dic['where']:
        for staff_item in staff_info:
            if select_dic['where'][2] in staff_item[select_dic['where'][0]]:
                select_staff_info.append(staff_item)

    if select_dic['select'][0].strip() == '*':#如果是*查询，则打印查询到的员工的全部信息
        for i in select_staff_info:
            print(' '.join(list(i.values())))
    else:#否则，如果指定列名查询，则打印查询到员工的指定列名信息
        for i in select_staff_info:
            li = []
            for j in select_dic['select']:
                li.append(i.get(j))
            print(' '.join(li))


#用户登陆，限3次尝试机会
login_count = 0
while login_count <= 3:#用户登陆
    username = input('请输入登陆用户名（liusl）：')
    password = input('请输入登陆密码(123456)：')
    if login(username, password):
        print('登陆成功!')
        break
    else:
        login_count += 1
        print('账号密码错误，请重新输入')
        continue
else:
    print('失败次数过多，账号已锁定')


#输入查询语句，输出查询结果
select_comm = input('请输入你的查询语句：')
statement_run(select_comm)#输入查询语句














