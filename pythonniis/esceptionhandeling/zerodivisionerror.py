print("main start")
L=[10,20,30]
try:
 print(L[2]//2)
except Indexerror as e:
	print("hi",e)
except Zeroxdivisionerror as e:
	print("bye",e)
except:
	print("handle all exception")
print("main end")