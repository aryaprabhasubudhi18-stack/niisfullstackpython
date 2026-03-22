from abc import *
class shape(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def area(self):
        pass
class Rectangle(shape):
    def __init__(self, n, l, b):
        super().__init__(n)
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b
class Square(shape):
    def __init__(self, n, l):
        super().__init__(n)
        self.l = l
    def area(self):
        return self.l * self.l
r1 = Rectangle("rect", 5, 7)
print("Rectangle Area:", r1.area())
s1=Square("sq",7)
print(s1.area())