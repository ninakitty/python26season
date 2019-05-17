'''
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
'''

column_dic = {'id':0,'name':1,'age':2,'phone':3,'job':4}

def func_filter(operate,condition):  # in  phone in 133
    '''

    :param operate: >/</==/in
    :param condition: age>22 /age==22 /phone in 133
    :return: 以字典的形式返回选择的条目
    '''
    select_list = []
    column,value = condition.split(operate)  #age 22
    column = column.strip()  #age
    value = value.strip()    #22
    if operate == '>':
        judge = 'int(line_list[column_dic[column]]) > int(value)'
    elif operate == '<':
        judge = 'int(line_list[column_dic[column]]) < int(value)'
    elif operate == '==':
        judge = 'line_list[column_dic[column]] == value'
    elif operate == 'in':
        judge = 'value in str(line_list[column_dic[column]]) '

    f = open('staff_info',mode='r',encoding='utf-8')
    for line in f:
        line_list = line.strip().split(',')

        #使用内置函数，从列表中得到符合条件的列表
        if eval(judge):
            select_list.append(line_list)
    f.close()
    return select_list

def func_get_line(con):
    '''
    :param con:例如 age>22
    :return: 以字典的形式返回选择的条目，
    '''
    if '>' in con:
        select_list = func_filter('>', con)
    elif '<' in con:
        select_list = func_filter('<', con)
    elif '=' in con:
        select_list = func_filter('==', con.replace('=','=='))
    elif 'like' in con:
        select_list = func_filter('in', con.replace('like','in'))
    return select_list


def func_get_show_column(con):
    '''

    :param con: select age,name/select *
    :return:以字典形式 返回查询的内容
    '''
    sp_sel_lst = con.strip().split('select')
    get_column_lst = []
    for item in sp_sel_lst:
        if item:
            if item.strip() == '*':
                return column_dic.keys()
            else:
                sp_d_lst = item.strip().split(',')
                for a in sp_d_lst:
                    get_column_lst.append(a)
                return get_column_lst
                

def fun_user_select_column(show_column_lst,select_lst):
    '''
    :param show_column_lst: 列符合条件的列表
    :param select_lst: 整行符合条件的内容列表
    :return:
    '''
    for line in select_lst:
        for key in show_column_lst:
            print(line[column_dic[key]],end=' ')
        print('')



select_input = input('>>>')
ret_lst = select_input.split('where')

# phone like 133
condition = ret_lst[1].strip()


#得到符合条件的整行内容
select_lst = func_get_line(condition)

# ret[0]  select name, age
show_column_lst = func_get_show_column(ret_lst[0])

#显示用户所要查询的内容
show_user_select_column = fun_user_select_column(show_column_lst,select_lst)