#!/usr/bin/env python

sum = 0
count = 0

while count < 99:
    count += 1

    if count%2 == 0:
        even_number = count
        sum = sum - even_number

    elif count%2 == 1:
        uneven_number =  count
        sum = sum + uneven_number


print(sum)