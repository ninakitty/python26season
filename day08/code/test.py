# a = 'nihao'
#
# print(len(a))
# import struct
#
# a = 50
# # print(str(a).encode('utf-8'))
# ret = struct.pack('i',a)
# print(ret,len(ret))
#
# print(struct.unpack('i',ret)[0])

import os

ret = os.urandom(32)
print(ret,len(ret))




