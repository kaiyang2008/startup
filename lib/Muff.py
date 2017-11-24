class Muff:
    def __init__(self,r=False):
        self.muff = r
    def cal(self,expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muff:
                print("Division by zero is illegal")
            else:
                raise
