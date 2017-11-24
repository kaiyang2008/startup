#!/usr/bin/python3


str1 = "This is testing for python"
str2 = "www.google.com"

list1 = str1.split("is")

print(list1)

list2=str2.split(".")[1]
print(list2)

from string import Template

tmp = Template("Hello, $who! $what enough for ya?")

str3= tmp.substitute(who="Mars",what="Dysty")

print(str3)

print("{0},{1} and {2}".format("first","second","third"))


from math import pi

print("{name} is approximatedly {value:.2f}".format(value=pi,name="pi"))

print("{foo} {} {bar} {}".format(1,2,foo=3,bar=4))

fullname = ["Alfred","Smoketoomuch"]

print("Hellow Mr {name[1]}".format(name=fullname))

import math
tmp = "The {mod.__name__} module defines the value {mod.pi} for u"
print(tmp.format(mod=math))


sep="/"

array1 = ["","usr","bin","python"]

str4 = sep.join(array1)
print(str4)


name="KAIY"
names=["kaiy","snps"]

if name.upper() in names:
    print("found {} in names".format(name.lower()))
else:
    print("not found {} in names".format(name))


str5 = "that's all forks"
import string
title_str = string.capwords(str5)
print("'{}' title string is '{}'".format(str5,title_str))
