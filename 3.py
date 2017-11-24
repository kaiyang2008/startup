#!/usr/bin/python3

dict1 = {"hello":322,"snps":333}

print("hello value in dict is {hello}".format_map(dict1))


dict2 = dict(name="kaiy",age=32)
y=dict2.copy()

print(dict2)

for k in dict2.keys():
    print("{} : {}".format(k,dict2[k]))


dict2={}
print(dict2)
print(y)

dict2.clear()
print(y)
print(dict2)

dict3=dict.fromkeys(['name','age'],'(unknown)')
print(dict3)

for k,v in dict1.items():
    print("{} : {}".format(k,v))

print("")
for k in dict1.keys():
    print("{} : {}".format(k,dict1[k]))
