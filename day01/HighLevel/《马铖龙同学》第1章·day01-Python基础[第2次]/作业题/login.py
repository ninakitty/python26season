#!/usr/bin/env python
# -*- coding:UTF-8 -*-

Name = "mcl"
Passwd = "mcl"
Count = 0

while Count < 3:
	User = input("请输入用户名:")
	if Name == User:
		while Count < 3:
			User_passwd = input("请输入密码:")
			if Passwd == User_passwd:
				print("恭喜您，你登录成功了")
				break
			else:
				Count += 1
				print("登录失败，密码错误，你还剩%s次机会" %(3 - Count))
		break
	else:
		Count += 1
		print("登录失败，用户名错误，你还剩次%s机会" %(3 - Count))
