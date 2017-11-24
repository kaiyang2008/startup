#!/usr/bin/python3

fibs= [ 0,1]

for i in range(10):
    fibs.append(fibs[-2] + fibs[-1])


print(fibs)


def fibs(num):
    'Calculate fibs'
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result


res = fibs(10)

print(res)
print(fibs.__doc__)


name = "kaiy"
n=name
print(id(name),id(n))

n="snps"
print(id(name),id(n))


def change(n):
    n[0] = "snps"

names=["kaiy","hello"]

change(names)

print("names is {}".format(names))


def print_p(**params):
    print(params)

print_p(x=1,y=2,z=3)


def with_star(**kwds):
    print("{name} is {age} years old".format_map(kwds)) ## using format_map to get dict key and value to print
    #print("{} is {} years old".format(kwds["name"],kwds["age"]))
args = {"name":"kaiy","age":35}
#with_star(**args)


x=1
def change_global():
    global x
    x+=1

change_global()
print("x",x,sep="=")


def foo():
    def bar():
        print("hello in bar")
    bar()

foo()

def multi(factor):
    def multiplay(number):
        return number * factor
    return multiplay

xx = multi(2)(2)
print("xx is",xx)
