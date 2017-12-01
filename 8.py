#!/usr/bin/python3

#try:
#    x = int(input("Please enter a number:"))
#    y = int(input("Please enter a number:"))
#    print(x/y)
#except ZeroDivisionError:
#    print("The second number can't be zero!")

import sys

sys.path.append("~/work/python/begin_python/1/lib")

from lib.Muff import Muff
#import Muff
#import lib
from lib import Muff

m = Muff.Muff()
#m = Muff(True)

m.cal("9/0")
