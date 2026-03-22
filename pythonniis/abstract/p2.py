from abc import *
class shape(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(shape):
    def __init__(self, n, l, b):
        super().__init__(n)
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b
    def perimeter(self):
        return 2 * (self.l + self.b)
class Square(shape):
    def __init__(self, n, l):
        super().__init__(n)
        self.l = l
    def area(self):
        return self.l * self.l
    def perimeter(self):
        return 4 * self.l
r1 = Rectangle("rect", 5, 7)
print("Rectangle Area:", r1.area())
print("Rectangle Perimeter:", r1.perimeter())
s1 = Square("sq", 7)
print("Square Area:", s1.area())
print("Square Perimeter:", s1.perimeter())