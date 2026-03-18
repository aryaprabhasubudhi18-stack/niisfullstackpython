class Rectangle:
	def __init__(self,l,b):
		self.length=l
		self.breadth=b
	def show(self):
		print("length=",self.length)
		print("breadth=",self.breadth)
	def area(self):
		return self.length*self.breadth
	def perimeter(self):
		print("perimeter=",2*(self.length+self.breadth))
r1=Rectangle(20,10)
r1.show()
print("area of Rectangle=",r1.area())
r1.perimeter()
	