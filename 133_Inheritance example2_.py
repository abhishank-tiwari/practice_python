#Multi level Inheritance
class A:
	def feature1(self):
		print("Feature 1 is working")
	
	def feature2(self):
		print("Feature 2 is working")

class B(A):
	def feature3(self):
		print("Feature 3 is working")
	
	def feature4(self):
		print("Feature 4 is working")
		
class C(B):
	def feature5(self):
		print("Feature 5 is working")
	
	def feature6(self):
		print("Feature 6 is working")

		
a1 = A()
print("Reaching class A(Super Class)")
a1.feature1()
a1.feature2()
b1 = B()
print("Reaching class B(Sub class of A)")
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
c1 = C()
print("Reaching class C(Sub class of B)")
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()