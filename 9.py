#!/usr/bin/python3

import sys

def describe_p(person):
    print('Descript of ',person['name'])
    print('Age: ', person['age'])
    try:
        print('Occupation:',person['occupation'])
    except KeyError:
        print("No occupation key")

person = { "name":"kaiy","age":42}
person["occupation"] = "IT"

describe_p(person)

