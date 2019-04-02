#
# s = "胡辣汤"  # unicode -> 定长
# #对字符串s进行编码
# # bytes
# # b'\xe8\x83\xa1\xe8\xbe\xa3\xe6\xb1\xa4'  utf-8
# # b'\xba\xfa\xc0\xb1\xcc\xc0'  gbk
# bs = s.encode("gbk") # 把字符串变成utf-8
# print(bs)

# # 解码
# # 把byte变回文字
# bs = b'\xe8\x83\xa1\xe8\xbe\xa3\xe6\xb1\xa4'
# s = bs.decode("utf-8") # 用什么编码就必须用什么解码
# print(s)

s = "abcd哈哈哈"
bs = s.encode("gbk")
print(bs)

# bytes:英文还是英文,. 中文变成\x  最小的数据单位
