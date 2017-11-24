class Person():
    def __init__(self,name="kaiy"): 
        self.name = name

    def set_name(self,name):
        self.name = name

    def get_name(self,name):
        return self.name

    def greet(self):
        print("Hello, world! I'm {}".format(self.name))
