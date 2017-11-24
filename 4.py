#!/usr/bin/python3

a,*rest,b= [1,2,3,4,5]

print(rest)


mul = [ x * x for x in range(10) if x % 3 == 0]

print(mul)


girls = [ "alice","bernice","clarice"]
boys  = [ "chris","arnold","bob"]

com = [ b +  "+ " + g for b in boys for g in girls if b[0] == g[0]]
print(com)


squ = {i: "{} sque is {}".format(i,i**2) for i in range(10)}

print(squ)

