username = 'zoujitao'
password = '123456'
count = 3
while count > 0:
    name = input('����������˻���')
    if name == username:
        paword = input('������������룺')
        if paword == password:
            print('��¼�ɹ�')
            exit(0)
        else:
            count = count - 1
            if count == 0:
                print('�˻�����������������Ѿ�û�л����ˣ�game over...')
            else:
                print('�˻���������������㻹��%s����' % (count))
    else:
        count = count - 1
        if count == 0:
            print('�˻�����������������Ѿ�û�л����ˣ�game over...')
        else:
            print('�˻���������������㻹��%s����' % (count))