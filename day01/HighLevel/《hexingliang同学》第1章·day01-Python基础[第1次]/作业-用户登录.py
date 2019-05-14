count = 1
us_name = "xliang"
us_pwd  = "123123"
while count < 4:
     name = input("用户名>>> ")
     pwd  = input("密码>>> ")
     if (name == us_name and pwd == us_pwd):
         print("登陆成功......")
         break
     else:
         count = count + 1
         err_count = 4 - count
         if err_count == 0:
             print("连续错误3次账户被锁定，请稍后再试...")
         else:
             print("用户名或密码错误，您还可以尝试登陆" + str(err_count)  + "次")


# 问题：为什么print 里面的变量如果不转换为字符串，会提示报错呢。print 必须要字符串类型吗。 不转换提示:must be string not int