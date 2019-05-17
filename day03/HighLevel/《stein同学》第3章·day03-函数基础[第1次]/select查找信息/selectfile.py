# -*- coding:utf-8 -*-

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
# select name,age where age > 22
# select * where job = IT
# select * where phone like 133

def select_index(select):
    res = select.strip().split(' ')
    if res[3] == 'id':
        return 0
    elif res[3] == 'name':
        return  1
    elif res[3] == 'age':
        return  2
    elif res[3] == 'phone':
        return  3
    elif res[3] == 'job':
        return  4

def select(select):
    res = select.strip().split(' ')
    l = []
    count = 0
    if res[1] == '*':
        if res[4] == '>':
            
            with open('fileinfo', mode='r', encoding='utf-8') as f:
                for i in f:
                    if count > 0:
                        resu = i.strip().split(',')
                        s = select_index(select)
                        if int(resu[s]) > int(res[5]):
                            l.append(resu)
                    count += 1
                return  l

        elif res[4] == '<':
            
            with open('fileinfo', mode='r', encoding='utf-8') as f:
                for i in f:
                    if count > 0:
                        resu = i.strip().split(',')
                        s = select_index(select)
                        if int(resu[s]) < int(res[5]):
                            l.append(resu)
                    count += 1
                return l

        elif res[4] == '=':
            
            with open('fileinfo', mode='r', encoding='utf-8') as f:
                for i in f:
                    if count > 0:
                        resu = i.strip().split(',')
                        s = select_index(select)
                        if resu[s] == res[5]:
                            l.append(resu)
                    count += 1
                return l

        elif res[4] == 'like':
            
            with open('fileinfo', mode='r', encoding='utf-8') as f:
                for i in f:
                    if count > 0:
                        resu = i.strip().split(',')
                        s = select_index(select)
                        # if resu[s].startswith(res[5]):
                        if res[5] in resu[s]:
                            l.append(resu)
                    count += 1
                return l

    else:
        if res[4] == '>':
            
            with open('fileinfo', mode='r', encoding='utf-8') as f:
                for i in f:
                    if count > 0:
                        resu = i.strip().split(',')
                        s = select_index(select)
                        if int(resu[s]) > int(res[5]):
                            lis = res[1].split(',')
                            for i in lis:
                                if i == 'id':
                                    i1 = 0
                                elif i == 'name':
                                    i1 = 1
                                elif i == 'age':
                                    i1 = 2
                                elif i == 'phone':
                                    i1 = 3
                                elif i == 'job':
                                    i1 = 4
                                l.append(resu[i1])
                    count += 1
                return l

        if res[4] == '<':
            
            with open('fileinfo', mode='r', encoding='utf-8') as f:
                for i in f:
                    if count > 0:
                        resu = i.strip().split(',')
                        s = select_index(select)
                        if int(resu[s]) < int(res[5]):
                            lis = res[1].split(',')
                            for i in lis:
                                if i == 'id':
                                    i1 = 0
                                elif i == 'name':
                                    i1 = 1
                                elif i == 'age':
                                    i1 = 2
                                elif i == 'phone':
                                    i1 = 3
                                elif i == 'job':
                                    i1 = 4
                                l.append(resu[i1])
                    count += 1
                return l

        if res[4] == '=':
            
            with open('fileinfo', mode='r', encoding='utf-8') as f:
                for i in f:
                    if count > 0:
                        resu = i.strip().split(',')
                        s = select_index(select)
                        if resu[s] == res[5]:
                            lis = res[1].split(',')
                            for i in lis:
                                if i == 'id':
                                    i1 = 0
                                elif i == 'name':
                                    i1 = 1
                                elif i == 'age':
                                    i1 = 2
                                elif i == 'phone':
                                    i1 = 3
                                elif i == 'job':
                                    i1 = 4
                                l.append(resu[i1])
                    count += 1
                return l

        if res[4] == 'like':
            
            with open('fileinfo', mode='r', encoding='utf-8') as f:
                for i in f:
                    if count > 0:
                        resu = i.strip().split(',')
                        s = select_index(select)
                        if res[5] in resu[s]:
                            lis = res[1].split(',')
                            for i in lis:
                                if i == 'id':
                                    i1 = 0
                                elif i == 'name':
                                    i1 = 1
                                elif i == 'age':
                                    i1 = 2
                                elif i == 'phone':
                                    i1 = 3
                                elif i == 'job':
                                    i1 = 4
                                l.append(resu[i1])
                    count += 1
                return l

aa = "select * where name like l"  #select name,age where age > 22
print(select(aa))




