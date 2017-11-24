#!/usr/bin/python3

print("hello world")

print \
("this is testing")

string1 = "this is testing for slash \
and here is second line"
print(string1)


path = "C:\\nown"

print(path)


print(r"C:\nown_now" "\\")
string2 = "hello"

print(string2[0])
#year = input("Year: ")
#print(year)


endings = ['st','nd','rd'] + ['th'] * 17
print(endings)


array = ["hello","world"]

for i in array:
    print(i)

database = [
    ['kaiy','123'],
    ['snps','234']
]

user=input("user:")
pin=input("pin:")

if [user,pin] in database:
    print("correct")
else:
    print("not correct")

tup = (1,2.3,["hello","world"])
tup1 = (4,["hello","world"])

print(tup[1])

print(tup[2][0])
tup[2][0]="hi"
print(tup[2][0])
print(tup)
tup3 = tup + tup1
print(tup3)

list1 = [3,1,4]
list1.sort()
print(list1)
list2 = sorted(list1)
print(list2)
