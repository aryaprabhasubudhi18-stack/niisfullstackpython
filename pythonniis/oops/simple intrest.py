class simple:
	def __init__(self,p,t,r):
		self.principal=p
		self.time=t
		self.rate=r
	def show(self):
		print("principal=",self.principal)
		print("my time=",self.time)
		print("my rate=",self.rate)
	def sical(self):
		return self.principal*self.rate*self.time/100
s1=simple(1000,10,2)
s1.show()
print("simple intrest=",s1.sical())