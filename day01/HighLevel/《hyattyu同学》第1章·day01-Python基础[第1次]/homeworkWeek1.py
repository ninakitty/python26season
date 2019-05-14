count = 0
CorrectUsername = "Hyatt.yu"
CorrectPassWord = "123456"
def VerifyUserInfo(username,password):
	if username==CorrectUsername and password==CorrectPassWord:
		return True
	else:		
		return False
	
def LoginFunc():
	InputUserName = input("please input username: ")
	InputPassWord = input("please input password: ")
	return (InputUserName,InputPassWord)

def main():	
	UserName,PassWord = LoginFunc()
	if VerifyUserInfo(UserName,PassWord):
		print("login success")
	else:
		global count
		count = count + 1
		if count<3:
			RemainTimes = str(3 - count)
			print("login fail, still have " + RemainTimes + " times")
			main()
		else:
			return

main()
	
	
