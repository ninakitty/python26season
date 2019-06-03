dic = [{1: 2}, {2: 3}]
for item in dic:
    for key, value in item.items():
        print(key, value)
import os


def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size


os.chdir(os.pardir)
res=getdirsize('test')
print(res)
