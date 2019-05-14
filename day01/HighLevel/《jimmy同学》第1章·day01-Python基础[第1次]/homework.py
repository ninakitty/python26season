x = 1
while x <= 4 :
	pd = input('请输入密码：')
	if pd != '123abc' :
		print("剩余错误次数：" + str(4 - x))
	x = x + 1