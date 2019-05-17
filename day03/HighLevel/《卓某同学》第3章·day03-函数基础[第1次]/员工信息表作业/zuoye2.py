def select():
    print('''select name,age where age > 22
select * where job = IT
select * where phone like 133''')
    user_input = input('请输入如上查询语句>>>')
    user_input = user_input.strip().split(' ')#将用户输入的语句分割成列表
    if user_input[4] == '=':
        with open('info.txt', mode='r', encoding='utf-8') as f:
            first_line = f.readline().strip().split(',')
            ind = first_line.index(user_input[3]) #获取=前面的角标
            for line in f:
                new_line = line.strip().split(',')
                if new_line[ind] == user_input[5]:
                    print(line)

    elif user_input[4] == '>':
        with open('info.txt', mode='r', encoding='utf-8') as f:
            first_line = f.readline().strip().split(',')
            ind = first_line.index(user_input[3]) #获取>前面的角标
            tj_s = user_input[1]#获取要查看的所有字段
            tj_s1 = []#列表形式存放每一个要查看的字段
            tj_ind = []#列表形式存放每一个要查看的字段的角标
            if ',' in tj_s:
                tj_s = tj_s.split(',')#有多个字段
                for i in tj_s:
                    tj_s1.append(i)#添加存放每一个要查看的字段
            else:#只有一个字段
                tj_s1.append(user_input[1])
            for i in tj_s:
                tj_ind.append(first_line.index(i))#添加要查看字段的角标
            for line in f:
                new_line = line.strip().split(',')
                if new_line[ind] > user_input[5]:
                    for i in tj_ind:
                        print(new_line[i])

    elif user_input[4] == 'like':
        with open('info.txt',mode='r',encoding='utf-8') as f:
            f.readline()
            for line in f:
                new_line = line.strip().split(' ')
                if str(user_input[5]) in line: #判断like后面的内容是否在行中
                    print(line)
select()