#!/usr/bin/env python
# coding: utf-8

"""
Created by zwb on 2018/9/5
1. 支持增删改查;
2. 支持作业要求3种查询语法;
3. 增加记录，员工id自增;
2. 删除和修改的条件需指定的字段匹配(索引字段), 作业要求是指定id删除，改为按照where条件来删除(此实现可以批量删除,更具挑战);
3. 增删改需要用户名和密码验证, 查询不需要身份认证, 通过装饰器实现;
"""

import re
import os

def query(filename,sql):
    index_list = []
    filed = sql.split()[1].split(",")
#    print("sql: {0}".format(sql))
#    print("filed: {0}".format(filed))
    condition = sql.split()[3:]
    ret = []
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n')
            if line.startswith("id"):
                 line_memu = line
                 for key in filed:
                     if key == "*":
                         break
                     else:
                         num = line.split(',').index(key)
                         index_list.append(num)
            else:
                if "like" in condition:
                    query_key = condition[0]
                    query_value = condition[2]
                    line_value = line.split(',')[line_memu.split(',').index(query_key)]
                    if query_value in line_value:
                        ret.append(line)
                        continue
                elif ">" in condition[0]:
                    query_key = condition[0].split(">")[0]
                    query_value = condition[0].split(">")[1]
                    line_value = line.split(',')[line_memu.split(',').index(query_key)]
                    #print("query_key:{0} query_value:{1} line_value:{2}".format(query_key, query_value, line_value))
                    if int(line_value) > int(query_value):
                        ret.append(line)
                elif "=" in condition[0]:
                    query_key = condition[0].split("=")[0]
                    query_value = condition[0].split("=")[1]
                    #print(line_memu.split(','))
                    line_value = line.split(',')[line_memu.split(',').index(query_key)]
                    #print("query_key:{0} query_value:{1} line_value:{2}
                    # index:{3}".format(query_key, query_value, line_value, line_memu.split(',').index(query_key)))
                    if query_value == line_value:
                        ret.append(line)
                elif "<" in condition[0]:
                    query_key = condition[0].split("<")[0]
                    query_value = condition[0].split("<")[1]
                    line_value = line.split(',')[line_memu.split(',').index(query_key)]
                    if int(line_value) < int(query_value):
                        ret.append(line)
                continue

    if len(index_list) == 0:
        return '\n'.join(ret)
    else:
        result = []
        for line in ret:
            mid_list = []
            str = ""
            for i in index_list:
                str = str + "," + line.split(',')[i]
            result.append(str.strip(','))
        return '\n'.join(result)
                
    return result


def add_record(filename,sql):
    line = sql.split(" ")[2]
    with open(filename, mode='r+', encoding='utf-8') as f:
        all_list = f.readlines()
        last_line = all_list[-1]
        id = int(last_line.split(',')[0]) + 1
        line = "{0},{1}".format(id, line)
        print(line)
        if last_line.endswith("\n"):
            f.write("{0}".format(line))
        else:
            f.write("\n{0}".format(line))
        return "update success"

def delete_line(filename, cond):
    bak = "{0}_bak".format(filename)
    with open(filename,mode='r', encoding='utf-8') as f1,open(bak, mode='w',
                                                              encoding='utf-8') as f2:
        if ">" in cond:
            value = cond.split(">")[1]
            for line in f1:
                if line.startswith("id"):
                    f2.write(line)
                    continue
                elif int(line.split(",")[2]) > int(value):
                    continue
                f2.write(line)
        if "=" in cond:
            value = cond.split("=")[1]
            for line in f1:
                if line.startswith("id"):
                    f2.write(line)
                    continue
                elif int(line.split(",")[2]) == int(value):
                    continue
                f2.write(line)
        if "<" in cond:
            value = cond.split("<")[1]
            for line in f1:
                if line.startswith("id"):
                    f2.write(line)
                    continue
                elif int(line.split(",")[2]) < int(value):
                    continue
            f2.write(line)
    os.remove(filename)
    os.rename(bak, filename)
    return "delete record success"

def delete_record(filename, sql):
    line = sql.split(" ")
    if len(line) == 2 and line[1] == "*" and line[0] == "delete":
        f = open(filename, mode='w')
        f.close()
        return "delete all record success"
    elif line[1] == "*" and line[0] == "delete":
        cond = line[3]
        ret = delete_line(filename, cond)
    return ret

def update_line(filename,cond, cond1):
    bak = "{0}_bak".format(filename)
    u_key = cond1.split('=')[0]
    u_value = cond1.split('=')[1]
    with open(filename,mode='r', encoding='utf-8') as f1,open(bak, mode='w+',
                                                              encoding='utf-8') as f2:
        if "=" in cond:
            cond_value = cond.split("=")[1]
            cond_key = cond.split("=")[0]
            for line in f1:
                line = line.strip("\n")
                if line.startswith("id"):
                    first_line = line.split(",")
                    indx = first_line.index(cond_key)
                    indx1 = first_line.index(u_key)
                    f2.write("{0}\n".format(line))
                    continue
                elif line.split(",")[indx] == cond_value:
                    line = line.split(',')
                    line[indx1] = u_value
                    line = ','.join(line)
                f2.write("{0}\n".format(line))
    os.remove(filename)
    os.rename(bak, filename)
    return "update record success"

def update(filename, sql):
    line = sql.split(" ")
    if line[0] == "set":
        cond1 = line[1]
        cond = line[3]
        ret = update_line(filename, cond, cond1)
    return ret



def auth2():
    def auth(func):
        def wrapper(*args,**kwargs):
                username=input("username: ")
                password=input("password: ")
                if username == 'derienzhang' and password=='123':
                    print('auth successfull')
                    res=func(*args,**kwargs)
                    return res
                else:
                    print("auth error")
        return wrapper
    return auth

@auth2()
def login():
    print('welcome to 运维中心.')


if __name__ == '__main__':
    filename = "com_info.txt"
    #sql = "select name,age where age>22"
    #sql = "select * where age>23"
#    sql = "select * where age<23"
#    sql = "select name,age where age<23"
    #sql = "select * where job=IT"
#    sql = "select name,age where job=IT"
#    sql = "select * where phone like 133"
#    sql = "select name,age where phone like 133"

#    sql = "set age=20 where phone like 133"
#    sql = "insert into 'tangsen',30,1363535322,'IT'"
#    sql = "delete * where age>25" # 目前只支持age条件删除
#    sql = "set age=23 where job='IT'" # 目前只支持job条件修改
    msg = '''
    例子：
    查询：
     select name,age where age>22
     select * where job=IT
     select * where phone like 133
     
    增加：
     insert into 'tangsen',30,1363535322,'IT'
    
    删除：
     delete * where age>25 # 目前只支持age条件删除
    
    更改：
     set age=18 where job=IT # 目前只支持job条件修改
    '''
    sql = input("{0}\nmysql>>>".format(msg)).strip()
    if sql.startswith("select"):
        ret = query(filename, sql)
    else:
        login()
        if sql.startswith("insert"):
            ret = add_record(filename, sql)
        elif sql.startswith("delete"):
            ret = delete_record(filename, sql)
        elif sql.startswith("set"):
            ret = update(filename, sql)
    print("{0}".format(ret))

