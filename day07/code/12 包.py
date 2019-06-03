# from admin import alex
#
# print(alex.name)
# alex.func()
# alex.Person()


# import admin # 默认admin就是__init__.py的内容
#
# print(admin.alex.name)
#
# import sys
# print(sys.path)


# import os
# os.makedirs('glance/api')
# os.makedirs('glance/cmd')
# os.makedirs('glance/db')
# l = []
# l.append(open('glance/__init__.py','w'))
# l.append(open('glance/api/__init__.py','w'))
# l.append(open('glance/api/policy.py','w'))
# l.append(open('glance/api/versions.py','w'))
# l.append(open('glance/cmd/__init__.py','w'))
# l.append(open('glance/cmd/manage.py','w'))
# l.append(open('glance/db/__init__.py','w'))
# l.append(open('glance/db/models.py','w'))
#
#
# map(lambda f:f.close() ,l)


# 调用policy中的func
#  from 后面的import不允许有   点

from glance.api import policy
policy.func()

# import glance # glance->__init__.py
# glance.api.policy.func()













