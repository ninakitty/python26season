#!/usr/bin/python
# -*- coding:utf-8 -*-
#select name, age where age>22
def fun1(age):
    if age.isdigit():
        with open(r'员工信息',encoding='utf-8') as f:
            for  line in f:
                if ',' in line:
                    new_line=line.strip().split(',')
                else:
                    new_line = line.strip().split('，')
                if new_line[2].isdigit():
                    if int(new_line[2])>int(age):
                        print(new_line[1],new_line[2])
    else:
        print("age值应为整数型")
age=input('请输入查询条件年龄：')
fun1(age)

# select * where job=IT
def fun2(job):
    with open(r'员工信息', encoding='utf-8') as f:
        for  line in f:
            if ',' in line:
                new_line=line.strip().split(',')
            else:
                new_line = line.strip().split('，')
            if new_line[4]==job:
                print(line.strip())

job=input('请输入查询条件工作：')
fun2(job)

# #select * where phone like 133
def fun3(phone):
    with open(r'员工信息', encoding='utf-8') as f:
            for  line in f:
                if ',' in line:
                    new_line=line.strip().split(',')
                else:
                    new_line = line.strip().split('，')
                if phone in new_line[3]:
                    print(line.strip())

phone=input('请输入查询条件：')
fun3(phone)

#可创建新员工记录，id要顺序增加
def adduser(name,age,phone,job):
    li=[]
    with open(r'员工信息', encoding='utf-8') as f:
            for  line in f:
                if ',' in line:
                    new_line=line.strip().split(',')
                else:
                    new_line = line.strip().split('，')
                li.append(new_line[0])
    with open(r'员工信息',mode='a', encoding='utf-8') as f:
        f.write('\n'+str(int(li[-1])+1)+','+name+','+age+','+phone+','+job)

name=input('请输入你的名字:')
age=input('请输入你的年龄:')
phone=input('请输入你的手机号码:')
job=input('请输入你的工作:')
adduser(name,age,phone,job)

