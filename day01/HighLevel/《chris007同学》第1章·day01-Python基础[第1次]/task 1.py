# 第一章作业
# 1. 三次重试机会
# 2. 每次输错误时显示剩余错误次数
lis=['oldboy','666']
i=0
while i<3:
    usename=input('请输入用户名').strip()
    pwd=input('请输入密码').strip()

    if usename==lis[0] and pwd==lis[1]:
        print('登陆成功')
        break
    else:print(('密码错误,你还有%d次机会')%(2-i))
    i+=1