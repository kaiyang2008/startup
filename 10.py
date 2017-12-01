#!/usr/bin/python3

class Foo():
    def __init__(self,value=42):
        self.somevar = value


class Bar(Foo):
    def set_val(self,val):
        self.somevar = val
    def get_val(self):
        return self.somevar 

foo = Bar()
print("var:",foo.somevar)

foo.set_val(50)

print("var:",foo.somevar)


class Bird():
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("Aaaahh...")
            self.hungry = False
        else:
            print("No, i am not hungry")


b = Bird()

b.eat()
b.eat()


class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = "Squawk!"
    def sing(self):
        print(self.sound)

s=SongBird()
s.sing()
s.eat()
s.eat()


class Rect():
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self,size):
        self.width = self.height = size

    def get_size(self):
        return self.width,self.height
    size = property(get_size,set_size)

r= Rect()
r.width = 10 
r.height = 5
r.size=150,100

print(r.width,r.height)


import pprint
dict2 = dict(name="bob",age=34)
pprint.pprint(dict2)


class Myclass():
    """ static method, there is no 'self' and if you want to
    call the method/variable in static method, you need to call <class_name>.<var>/<method>
    """

    var = 10
    @staticmethod
    def smeth():
        print("This is static method",Myclass.var)

    """ class method, there is no 'self' but the input is 'cls' which can call method/var
    using cls.<method>/<var>, avoid to hard code like static method
    """
    @classmethod
    def cmeth(cls):
        Myclass.smeth()
        print("This is class method ",cls.var,cls)

#Myclass.smeth()
#Myclass.cmeth()

a=Myclass()
#a.smeth()
a.cmeth()
