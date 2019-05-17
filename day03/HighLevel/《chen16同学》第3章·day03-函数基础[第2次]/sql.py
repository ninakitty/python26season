# -*- coding:utf-8 -*-
# !/usr/bin/python

# 周末大作业：实现员工信息表
# 文件存储格式如下：
# id，name，age，phone，job
# 1,Alex,22,13651054608,IT
# 2,Egon,23,13304320533,Tearcher
# 3,nezha,25,1333235322,IT
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

def select_1():
    f = open('信息表.txt', encoding ='utf-8')
    def select_2(sql):
        left, right = sql.split('where')     #将语句按where分割后进行判断

        if '*' in left and 'job' in right:     #语句含有job的判断
            left_1, right_1 = right.strip().split('=')   #语句where后面的条件分割
            right_1 = right_1.strip()
            for line in f:
                index = line.strip().split(',')
                job = index[4]
                if job == right_1:
                    print(line)

        elif '*' in left and 'phone' in right:     #语句含有phone的判断
            left_1, right_1 = right.strip().split('like')  #语句where后面的条件分割
            right_1 = right_1.strip()
            for line in f:
                index = line.strip().split(',')
                phone = index[3]
                if right_1 in phone:
                    print(line)

        elif 'age' in left and 'age' in right:   #语句含有age的判断
            if '=' in sql:
                left_1, right_1 = right.strip().split('=')
                right_1 = right_1.strip()
                for line in f:
                    index = line.strip().split(',')
                    age = index[2]
                    if right_1 == age:
                        print(line)

            if '>' in sql:
                left_1, right_1 = right.strip().split('>')
                right_1 = right_1.strip()
                for line in f:
                    index = line.strip().split(',')
                    age = index[2]
                    if right_1 < age:
                        print(line)

            if '<' in sql:
                left_1, right_1 = right.strip().split('<')
                right_1 = right_1.strip()
                for line in f:
                    index = line.strip().split(',')
                    age = index[2]
                    if right_1 > age:
                        print(line)

    sql = input('请输入查询语句：')
    val = select_2(sql)
    return val

select_1()