user_name = "zhangsan"
user_pwd = "123"
count = 4
while count>0:
	input_name = input("请输入用户名：")
	input_pwd = input("请输入密码：")
	if input_name != user_name or input_pwd != user_pwd:
		count = count -1
		print("用户名或密码错误，当前剩余输入次数为:",count)
	else:
		print("登录成功！！！")
		break
		