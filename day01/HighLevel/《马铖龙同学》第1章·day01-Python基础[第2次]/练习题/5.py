#!/usr/bin/env python

Num = 66

while True:
	Guess = int(input("请输入一个数字:"))
	if Guess == Num:
		print("你猜对了！！")
		break
	elif Guess > Num:
		print("你猜的值大了")
	else:
		print("你猜的值小了")
