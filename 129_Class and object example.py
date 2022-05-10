class computer:
	def __init__(self):
		self.name = "Abhishank"
		self.age = 31
	def update(self):
		self.age = 26
	def compare(self,other):
		if self.age == other.age:
			print("They have same age")
		else:
			print("They have different age")

c1 = computer()
c2 = computer()
c1.update()
print(c1.compare(c2))
c1.age = 31
print(c1.compare(c2)) 