number = 3
while number >= 0:
	user_name = input("请输入你的用户名: ")
	user_passwd = input("请输入你的密码: ")
	if user_name == "zhangji":
		if user_passwd == "123456":
			print("登陆成功")
			break
		else:
			print("用户名或密码错误," + "你还有" + str(number) + "次重试机会")
			number = number - 1
	else:
		str(print("用户名或密码错误," + "你还有" + str(number) + "次重试机会"))
		number = number - 1
if number < 0:
	print("登陆超时")