#!/usr/bin/python3


import sys
import os

print(sys.argv)
print(sys.path)
print(sys.platform)

args = sys.argv[1:]
print(id(args))
args.reverse()
print(id(args))
print(' '.join(args))


print(os.system("ls -al"))
print(filename())
