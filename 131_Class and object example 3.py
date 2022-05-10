class student:
	def __init__(self,name,rollno):
		self.name = name
		self.rollno = rollno
		self.lap = self.Laptop()
	def show(self):
		print(self.name,self.rollno)
	class Laptop:
		def __init__(self):
			self.brand = "HP"
			self.cpu = "i5"
			self.ram = "8 gb"
		def show(self):
			print(self.brand,self.cpu,self.ram)
s1 = student("abhishank",1)
print(s1.show())
l1 = s1.Laptop()
print(l1.show())