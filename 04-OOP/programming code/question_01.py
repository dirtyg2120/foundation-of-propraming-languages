from abc import ABC


class Exp(ABC):
    pass


class IntLit(Exp):
    def __init__(self, num=0.0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num = num

    def print(self):
        print(self.num)  # print number attribute

    def eval(self):
        return self.num


class FloatLit(Exp):
    def __init__(self, num=0.0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num = num

    def print(self):
        print(self.num)  # print number attribute

    def eval(self):
        return self.num


class UnExp(Exp):
    def __init__(self, operator, arg):
        self.operator = operator
        self.arg = arg

    def eval(self):
        if self.operator == "-":
            return -self.arg.eval()
        elif self.operator == "+":
            return self.arg.eval()


class BinExp(Exp):
    def __init__(self, left, operator, right, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operator = operator
        self.left = left
        self.right = right

    def eval(self):
        if self.operator == "+":
            return self.left.eval() + self.right.eval()
        elif self.operator == "-":
            return self.left.eval() - self.right.eval()
        elif self.operator == "*":
            return self.left.eval() * self.right.eval()
        elif self.operator == "/":
            return self.left.eval() / self.right.eval()


x = Exp()
a = IntLit(4)
b = FloatLit(2.0)
x = BinExp(a, "*", b)
x = BinExp(b, "-", x)
print(x.eval())
# print(type(x))
