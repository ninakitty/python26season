import pickle

lst = ["张一山", "李四", "王二麻子"]
# pickle.dump(lst, open("singer.dat", mode="wb"))

# bs = pickle.dumps(lst)
# f = open("singer.dat", mode="wb")
# f.write(bs)
# f.flush()
# f.close()

# obj = pickle.load(open("singer.dat", mode="rb"))
# print(obj)
# bs = b'\x80\x03]q\x00(X\t\x00\x00\x00\xe5\xbc\xa0\xe4\xb8\x80\xe5\xb1\xb1q\x01X\x06\x00\x00\x00\xe6\x9d\x8e\xe5\x9b\x9bq\x02X\x0c\x00\x00\x00\xe7\x8e\x8b\xe4\xba\x8c\xe9\xba\xbb\xe5\xad\x90q\x03e.'
# obj = pickle.loads(bs)
# print(obj)
