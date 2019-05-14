#!/usr/bin/env python
# -*- encoding:utf-8 -*-
'''
username=input('please name:')
password=input('password:')
if username=='max':
	if password=='123':
		print('登陆成功')
	else:
		print('密码错误')
else:
	print('用户名错误')			


name=input('请输入名字：')
age=input('请输入年龄：')
print('此用户的姓名： '+name+' 年龄 '+age)


s1='我'
s2='很坚强'
s3=s1+s2
print(s3)
print(s1+' '+s2)

print('good')


if 1>3:
	print('good')
else:
	print(0)	



word=input("道歉：")
if word=="i'am sorry":
	print('good')
else:
	print('not good')
	


num=input('请输入数字：')

num=int(num)

if 90<num<100:
	print('A')
elif 60<num<90:
	print('B')
elif num<60:
	print('C')



s1=100
s1=str(s1)
s2="200"

print(s1,s2,type(s1),type(s2))



name=input('请输入名字：')
password=input('请输入密码：')

if name=='max':
	if password=='123':
		print('welcome')
	else:
		print('password wrong')
else:
	print('wrong name')






count=1
while count<101:
	print(count)
	count=count+1




number=0
count=1

while count<101:
	number=number+count
	
	count=count+1
	print(number)

while True:
	print(111)
	print(222)
	continue
	print(666)




count=1

while count<100:
		if count>7:
			print(count)
			

name=input('>>>')

good=type(name)

print(good)



line1='文能提笔安天下,'
line2='武能上马定乾坤.'
line3='心存谋略何人胜,'
line4='古今英雄唯是君.'

print (line1+'\n'+line2+'\n'+line3+'\n'+line4)
		  
		  


number=input('请输入数字：')
number=int(number)

if number>66:
	print('猜测的结果大了')
if number<66:
	print('猜测的结果小了')
if number==66:
	print('猜测结果正确')


age=input('请输入自己的年龄：')
age=int(age)
if age<10:
	print('小屁孩')
elif 10<age<=20:
	print('青春期叛逆的小屁孩')
elif 20<age<30:
	print('开始混社会的小屁孩儿')
elif 30<age<40:
	print('体制看老大不小了，赶紧结婚小屁孩儿')
elif 40<age<50:
	print('家里有个不听话的小屁孩儿')
elif 50<age<60:
	print('马上变成不听话的老屁孩儿')
elif 60<age<70:
	print('活着还不错的老屁孩儿')
elif 70<age<90:
	print('人生就快结束了的一个老屁孩儿')
elif age>90:
	print('再见了这个世界')




test=input("请输入'麻花藤':")
if test=="麻花藤":
	print('真聪明')
else:
	print('你是傻逼么')




number=1
while number<11:
	print(number)
	number=number+1

num=0
number=1
while number<101:
	num=num+number
	number=number+1
	if number==101:
		print(num)



x=0
while x<100:
	x=x+1
	number=x%2
	if number==1:
		print(x)



x=1
while x<100:
	x=x+1
	number=x%2
	if number==0:
		print(x)


x=1
y=0
while x<100:
	y=y+x
	x=x+2
	if x==101:
		print(y)

a=2
b=0
while a<101:
	b=b+a
	a=a+2
	if a==102:
		print(b)
		
number=y-b
print(number)

'''


number=1
while number<4:
	name=input('请输入用户名:')
	times=3-number
	password=input('请输入密码：')
	if name=='max':
		if password	=='123456':
			print('欢迎')
		else:
			print('密码错误，剩余',times,'次')
			#用户名对了，密码错误，减少一次
		number=number+1
	else:
		print('无此用户，请重新输入')
		print('剩余',times,'次')
		number=number+1     
		#用户名错误，同样也减少一次，并且用户名错误和密码错误次数是累加的
	
		

		