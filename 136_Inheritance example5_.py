#MRO - Method Resolution Order
class A:
	def __init__(self):
		print(" In A init")
	
	def feature1(self):
		print("Feature 1 is working")
	
	def feature2(self):
		print("Feature 2 is working")

class B():
	def __init__(self):
		print(" In B init")
	
	def feature3(self):
		print("Feature 3 is working")
	
	def feature4(self):
		print("Feature 4 is working")
		
class C(A,B):
	def __init__(self):
		super().__init__()
		print(" In C init")
	
	def feature5(self):
		print("Feature 5 is working")
	
	def feature6(self):
		print("Feature 6 is working")
 
 
print("Making a object of class C")	
c1 = C()