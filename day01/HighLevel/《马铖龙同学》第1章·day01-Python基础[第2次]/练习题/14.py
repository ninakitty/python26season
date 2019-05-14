#!/usr/bin/env python
# -*- coding:UTF-8 -*-

count = 0
_sum = 0
while count <= 99:
	count +=1
	if count % 2 == 0:
		_sum = _sum - count
	else:
		_sum = _sum + count

print(_sum)
