#!/usr/bin/python3

def describe_p(person):
    print('Descript of ',person['name'])
    print('Age: ', person['age'])
    try:
        print('Occupation:',person['occupation'])
    except KeyError:
        pass

person = { "name":"kaiy","age":42}

describe_p(person)
