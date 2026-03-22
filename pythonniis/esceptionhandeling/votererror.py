class Votererror(BaseException):
	def __init__(self,name):
		super().__init__()
print("enter a age")
age=int(input())
if age>=18:
	print("eligible")
else:
	try:
	 raise Votererror("age not allow")
	except:
		print("not allow")
print("main end")