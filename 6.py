#!/usr/bin/python3

def bi_search(seq,number,lower,upper):
    if lower == upper:
        if number == seq[upper]:
            return number
        else:
            return None
    else:
        mid = (lower + upper) // 2
        if number > seq[mid]:
            return bi_search(seq,number,mid+1,upper)
        else:
            return bi_search(seq,number,lower,mid)

num = [ 1,2,3,4,5]
tof = 3
find = bi_search(num,3,0,4)

print("find ",find)
    

from random import choice

x = choice(["hello world",[1,2,3,4,5]])
a=x.count(3)
print("x is {} and count is {}".format(x,a))
