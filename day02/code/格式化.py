#
name = input("Name:")
score = input("score:")
job = input("Job:")


#
#
# info = '''
# ----------------info --------------
# Name: %s
# score : %.2f
# job : %s
# ''' %(name,float(score),job)
#
#
# #%s string
# # %d integer
# # %f  float
#
# print(info)


# 模板字符串

info = f'''
----------------info --------------
Name: {name}
score : {score}
job : {job}
'''  # 直接把变量放在字符中

print(info)