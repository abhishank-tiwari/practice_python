#Method Overriding
class A:
	def show(self):
		print("In A show")

		
class B(A):
	pass

class C(A):
	def show(self):
		print("In C show")

		
b1 = B()
b1.show()
c1 = C()
c1.show()