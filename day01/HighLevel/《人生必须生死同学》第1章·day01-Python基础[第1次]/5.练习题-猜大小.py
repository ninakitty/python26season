num = 66




while True:
    user_input = int(input('请输入你要猜的数字:  '))
    if user_input == num:
        print('恭喜你，猜对啦！')
        break
    if user_input > num:
        print('猜大了')
    if user_input < num:
        print('猜小了')

