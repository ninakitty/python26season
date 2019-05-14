#!/usr/bin/env python
# -*- coding:utf-8 -*-
i=3
while i>0:
	UserName=input('请输入用户名：')
	Password=input('请输入密码：')
	i=i-1
	s=str(i)
	if UserName=='admin' and Password=='123':
		print('登录成功')
		break
	elif s!='0':
		print('登录失败,用户名或者密码错误,您还有' + s + '次机会尝试')
else:
	print('三次机会已使用完,登录失败,帐号已锁定')