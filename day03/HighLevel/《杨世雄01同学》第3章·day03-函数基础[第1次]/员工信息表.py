#id，name，age，phone，job
import os
def add():#增加
    choice = input('请确认是否增加，y/n').strip()
    if choice == 'y':
        print('需要输入人员信息')
        name = input('请输入需要增加的人员姓名').strip()
        age = input('请输入需要增加的人员年龄').strip()
        phone = input('请输入需要增加的人员电话').strip()
        job = input('请输入需要增加的人员工作').strip()
    sta = True
    while sta:
        with open('员工信息表','r',encoding='utf-8') as f:
            lis = []
            for line in f:
                content = line
                lis.append(int(line[0]))
        res = max(lis)
        new_id = res+1
        with open('员工信息表','a',encoding='utf-8') as f2:
            conn = str(new_id) +','+name+','+str(age)+','+str(phone)+','+job
            f2.write(conn)
        choice = input('添加完成，请确认是否继续添加？y/n').strip()
        if choice.lower() == 'y':
            sta = True
        elif choice.lower() == 'n':
            sta = False
def delete():#删除
    choice = int(input('请输入需要删除的人员ID：').strip())
    with open('员工信息表', 'r', encoding='utf-8') as f:
        lis = []
        for line in f:
            content = line
            lis.append(int(line[0]))
    if choice in lis:
        with open('员工信息表', 'r', encoding='utf-8')as f1,open('员工信息表.bak', 'w', encoding='utf-8') as f2:
            for line in f1:
                if int(line[0]) == choice:pass
                f2.write(line)
        os.remove('员工信息表')
        os.rename('员工信息表.bak','员工信息表')
    else:
        print('你输入的ID不存在！')
def my_print(index,show_lis,id_lis,name_lis,age_lis,phone_lis,job_lis):#打印
    index = int(index)
    if '*' in show_lis:
        print(id_lis[index],',',name_lis[index],',',age_lis[index],',',phone_lis[index],',',job_lis[index])
    else:
        res = ''
        for i in show_lis:
            if i.strip().lower() == 'id':
                res = res.strip() +id_lis[index].strip()+','
            if i.strip().lower() == 'name':
                res = res.strip() + name_lis[index].strip() + ','
            if i.strip().lower() == 'age':
                res = res.strip() + age_lis[index].strip() + ','
            if i.strip().lower() == 'phone':
                res = res.strip() + phone_lis[index].strip() + ','
            if i.strip().lower() == 'job':
                res = res.strip() + job_lis[index].strip() + ','
        print(res)
def reviese():#修改，与删除类似，暂时未写
    pass
def search():#查找
    choice = input('请输入你要进行的查找选择').strip()
    with open('员工信息表', 'r', encoding='utf-8') as f:
        id_lis = []
        name_lis = []
        age_lis = []
        phone_lis = []
        job_lis = []
        for line in f:
            content = line.split(',')
            id_lis.append(content[0].strip())
            name_lis.append(content[1].strip())
            age_lis.append(content[2].strip())
            phone_lis.append(content[3].strip())
            job_lis.append(content[4].strip())
        choice_new = choice.split('where')
        condition = choice_new[1].strip()
        show = choice_new[0].replace('select','').strip()
        show_lis = show.split(',')
        condition_new = ''
        for i in condition:
            if not i.isalpha(): break
            condition_new = condition_new + i
        condition_choice = condition.replace(condition_new,'').strip()
        if condition_new.lower()== 'phone':
            phone_num = ''
            for i in condition_choice:
                if i.isdigit():
                    phone_num = phone_num+ i
            for index,i in enumerate(phone_lis):
                if phone_num in i:
                    my_print(index,show_lis,id_lis,name_lis,age_lis,phone_lis,job_lis)
        elif condition_new.lower() == 'age':
            symbol = ''
            symbol_num = ''
            for i in condition_choice:
                if i.isdigit():
                    symbol_num =symbol_num+i
                else:
                    symbol = symbol + i
            symbol = symbol.strip()
            symbol_num = int(symbol_num)
            for index,i in enumerate(age_lis):
                i = int(i)
                if symbol == '>':
                    if symbol_num < i:
                        my_print(index, show_lis, id_lis, name_lis, age_lis, phone_lis, job_lis)
                elif symbol == '<':
                    if symbol_num > i:
                        my_print(index, show_lis, id_lis, name_lis, age_lis, phone_lis, job_lis)
                elif symbol == '=':
                    if symbol_num == i:
                        my_print(index, show_lis, id_lis, name_lis, age_lis, phone_lis, job_lis)
        elif condition_new.lower() == 'job':
            job_info = ''
            for i in condition_choice:
                if i.isalpha():
                    job_info = job_info+ i
            job_info = job_info.strip()
            for index,i in enumerate(job_lis):
                if job_info == i:
                    my_print(index,show_lis,id_lis,name_lis,age_lis,phone_lis,job_lis)

def interactive():#用户交互
    print('欢迎使用员工信息表系统'.center(20,'*'))
    status = True
    count = 0
    while status and count < 3:
        username = input('请输入你的帐号:').strip()
        password = input('请输入你的密码:').strip()
        status = login(username,password)
        count +=1
    while not status:
        func_msg ={
            '增加':add,
            '删除':delete,
            '修改':reviese,
            '查找':search
        }
        for key in func_msg:
            print(key)
        choice = input('请输入你的选择，例如：增加').strip()
        func_msg[choice]()

def login(account,word):#登录认证

    content = {
'yang':'1234',
'alex':'250'
}
    if account in content:
        if word == content[account]:
            print('登录成功，欢迎光临')
            return False
        else:
            print('密码错误，请重试！')
            return True
    else:
        print('账号不存在，请重试')
        return True

if __name__ =='__main__':#主程序
    interactive()