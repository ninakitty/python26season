count=3
while count > 0:
	account = input ('请输入账号:')
	password = input ('请输入密码:')
	if account != 'account' and password != 'password' and count > 1:
		count-= 1	
		print ('账号或密码错误，请重新输入,还有%s次机会'%(count))
	elif count == 1:
		break
	else:
		count = 0
		print ('登陆成功')
		