# 03 work

## 1
```python
 result = []
 with open("a1.txt",encoding="utf-8") as f:
     tmp = f.readline()
     title = tmp.strip().split()
     for line in f.readlines():
         tmp_line = line.strip().split()
         tmp_dic = {}
         for (k,v) in zip(title,tmp_line):
             tmp_dic.update({k:v})
         result.append(tmp_dic)
    
print(result)
```
## 2 

```python
def fun1(str):
    tmp_dic = {'数字':0,"字母":0,"空格":0,"其它":0}
    for s in str:
        if s.isdigit():
            tmp_dic['数字'] += 1
        elif s.isalpha():
            tmp_dic['字母'] += 1
        elif s.isspace():
            tmp_dic["空格"] += 1
        else:
            tmp_dic["其它"] += 1
    return tmp_dic
```
## 3
```python
def func2(num1,num2):
    return num1 if num1 > num2 else num2

print(func2(100,44))
```
## 4
```python
def func4(dic):
    for k,v in dic.items():
        if len(v) > 2:
            dic[k] = v[:2]
    return dic

dic = {"k1": "v1v1", "k2": [11,22,33,44]}
print(func4(dic))
```
## 5
```python
def func5(lst):
    if not isinstance(lst,list):
        return -1
    ret = {}
    for i in range(len(lst)):
        ret[i] = lst[i]
    return ret

print(func5([11,22,33]))
```
## 6
```python
def func6(name,sex,age,level):
    str = f"{name} {sex} {age} {level}\n"
    with open("student_msg.txt","w",encoding="utf-8") as f:
        f.write(str)

func6('test','男',11,"本科")
```
## 7
```python
def func71(name,age,level,sex="男"):
    str = f"{name} {sex} {age} {level}\n"
    with open("student_msg.txt","a+",encoding="utf-8") as f:
        f.write(str)

def func7():
    while True:
        info = input("请输入学生信息：姓名 年龄 学历 性别 （输入Q或q退出）》》》\n").strip()
        if info == 'Q' or info == 'q':
            break
        name,age,level,sex = info.split()
        if sex == None:
            sex = '男'
        func71(name,age,level,sex)
func7()
```
## 8
```python
def func8(filename,old_str,new_str):
    with open(filename,'r+') as f:
        tmp = f.read()
        f.seek(0)
        tmp = tmp.replace(old_str,new_str)
        f.write(tmp)

func8("tmp.txt","aaa",'bbb')
```
## 9
 a: 20
 b: 10
 c: None


## 10
```python
def func10(*args):
    print(args)
func10(*[1,2,3],*(22,33))
```
## 11
```python
def func11(**kwargs):
    print(kwargs)
func11(**{'name':'zmf'},**{"age":'22'})
```
## 12

### 一

成立，打印2

### 二

不成立，将 a += 1 修改为 globals a += 1

### 三

成立，打印1

### 四

不成立，将 a += 1 修改为 nonlocal a += 1

## 13
```python
def func13(num1,num2):
    return num1 if num1 < num2 else num2

print(func13(100,44))
```
## 14
```python
def func14(arg):
    tmp = []
    for item in arg:
        tmp.append(str(item))
    return "_".join(tmp)

print(func14([1,'老男孩','武sir']))
```
## 15
```python
def min_max(*arg):
    return {'max':max(arg),'min':min(arg)}

print(min_max(1,3,54,6,7,42,-22))
```
## 16
```python
def cal(n):
    ret = 1
    for i in range(1,n+1):
        ret *= i
    return ret

print(cal(7))
```
## 17
```python
def puke():
    lst = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    lst2 = ["红桃","方片","黑桃","梅花"]
    ret = []
    for k in lst2:
        for v in lst:
            ret.append((k,v))
    return ret

print(puke())
```
## 18
```python
# def wrapper():
#     def inner():
#         print(666)
#     inner()
# wrapper()

def wrapper():
    def inner():
        print(666)
    return inner
f = wrapper()
f()
```