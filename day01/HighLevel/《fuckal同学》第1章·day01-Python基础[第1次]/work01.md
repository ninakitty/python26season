# practice 01
## 1、简述变量命名规范
1. 由数字字母下划线组成
2. 不能以数字开头
3. 不能与内置的关键字冲突
4. 命令格式可以参考PEP8
## 2、name = input(“>>>”) name变量是什么数据类型？
str
## 3、if条件语句的基本结构？
```python
if True:
    print("True")
elif 1 == 1:
    print("1 == 1")
else:
    print("else")
```
## 4、用print打印出下面内容：
    文能提笔安天下,  
    武能上马定乾坤.  
    心存谋略何人胜,  
    古今英雄唯是君. 
```python
print("""   文能提笔安天下,  
    武能上马定乾坤.  
    心存谋略何人胜,  
    古今英雄唯是君.""")
```
## 5、利用if语句写出猜大小的游戏：
设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测
的结果小了;只有等于66，显示猜测结果正确。
```python
num1 = 66
tmp_num = 0
print("猜大小游戏，数字在0-100之间，请输入一个数字")
while True:
    tmp_num = int(input(">>>："))
    if tmp_num > 66:
        print("您输入的数字太大了，请重新输入")
    elif tmp_num < 66:
        print("您输入的数字太小了，请重新输入")
    elif tmp_num == num1:
        print("恭喜，猜对了")
        break
```
## 6、提示用户输入他的年龄, 程序进?判断.
  如果小于10, 提示小屁孩, 如果大于10, 小于于 20, 提示青春期叛逆的小屁孩. 如果大于20, 小于30. 提
示开始定性, 开始混社会的小屁孩儿, 如果大于30, 小于40. 提示看老大不小了, 赶紧结婚小屁孩儿. 如果大
于40, 小于50. 提示家里有个不听话的小屁孩儿. 如果大于50, 小于60. 提示自己马上变成不听 话的老屁孩
儿.如果大于60, 小于70. 提示活着还不错的老屁孩儿. 如果大于70, 小于于 90. 提示人生就快结束了的一个
老屁孩儿. 如果大于90以上. 提示. 再见了这个世界. 
```python
age = int(input("请输入你的年龄："))
if age <= 10:
    print("小屁孩")
elif age > 10 and age <= 20:
    print("青春期叛逆的小屁孩")
elif age > 20 and age <= 30:
    print("开始定性，开始混社会的小屁孩")
elif age > 30 and age <= 40:
    print("看老大不小了，赶紧结婚的小屁孩")
elif age > 40 and age <= 50:
    print("家里有个不听话的小屁孩")
elif age > 50 and age <= 60:
    print("自己马上变成不听话的老屁孩")
elif age > 60 and age <= 70:
    print("活着还不错的老屁孩儿")
elif age > 70 and age <= 90:
    print("人生就快结束了的一个老屁孩儿")
elif age > 90:
    print("再见了这个世界"
```
## 7、单行注释以及多行注释？

```python
# 这个单行注释
'''
    这是多
    行注释
'''
"""
    这也是多
        行注释
"""
```
## 8、简述你所知道的Python3x和Python2x的区别？

Python3.x与Python2.x不兼容
print 语句变成了print函数
默认字符编码不一样
除法存在区别
Python3中去掉的<>不等运算符
异常部分存在区别
Python3中标识符甚至可以是中文
raw_input ==>　input
文件打开只能用open

## 9、提示用户输入麻花藤. 判断用户输入的对不对. 如果对, 提示真聪明, 如果不对, 提示你 是傻逼么
```python
if "麻花藤" == input("请输入麻花藤 >>>: "):
    print("真聪明")
else:
    print("你是傻逼么？")
```
## 10、使用while循环输入 1 2 3 4 5 6 8 9 10
```python
count = 0
tmp = []
while True:
    tmp.append(int(input(">>>: ")))
    count += 1
    if count == 10:
        break

for i in tmp:
    print(i)
```
## 11、求1-100的所有数的和
```python
sum = 0
for i in range(101):
    sum += i
print(sum)
```
## 12、输出 1-100 内的所有奇数
```python
for i in range(1,100,2):
    print(i
```
## 13、输出 1-100 内的所有偶数
```python
for i in range(0,101,2):
    print(i)
```
## 14、求1-2+3-4+5 ... 99的所有数的和
```python
sum = 0
for i in range(1,100,2):
    sum += i
for i in range(2,100,2):
    sum -= i

print(sum)
```
## 用户登陆

```python
import getpass

def Login():
try_count =  3  # 允许尝试的次数
pwd_dict = {"zmf96":"zmf97","admin":"admin123"}
print("***请输入用户名及密码***")
for i in range(try_count):
user_name = input("User: ")
user_pwd = getpass.getpass()
if user_name in pwd_dict.keys() and user_pwd == pwd_dict[user_name]:
print("【登陆成功】")
break
else:
print("【登陆失败】用户名或密码不正确，请重试（剩余尝试次数：{n})".format(n = try_count-i-1))

if __name__ ==  "__main__":
Login()
```