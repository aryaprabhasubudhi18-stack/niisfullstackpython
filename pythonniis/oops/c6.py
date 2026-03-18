class Demo:
	def __show(self): # private method
		print("hi")
	def disp(self):
		self.__show()
ob=Demo()
    #ob.__show()error
ob.disp()