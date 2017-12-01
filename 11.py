#!/usr/bin/python3


import sys
import pprint

def flattern(nested):
    try:
        for ele in nested:
            for i in ele:
                yield flattern(i)

    except TypeError:
        yield nested

nested_list = [[1,[2,3,4],[4,5]],6]

print(list(flattern(nested_list)))
