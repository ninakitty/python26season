#!/usr/bin/env python
# -*- coding: UTF-8 -*
#初始设置的用户和密码
user_name='djx'
user_password='123456'
i=0
while i<3:
	name=input("please input  you name :")
	password=input("please input  you password :")
	if name == user_name and password == user_password:
		print("login successfully ")
		break
	else:
		print("user name or password is wrong ")
		count=2-i
		print("There are still "  + str(count) +" landing opportunities left")
		i+=1