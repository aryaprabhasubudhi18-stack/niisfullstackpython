class Demo:
	def __init__(self,x,y): #method
		self.__x=x  #private instance variable
		self.__y=y  #private instance variable
	def show(self):
		print(ob.__x)
		print(ob.__y)
ob=Demo(10,20)
 #print(ob.__y)error
ob.show()