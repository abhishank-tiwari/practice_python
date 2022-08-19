class computer:
	def __init__(self):
		self.name = "Abhishank"
		self.age = 28
	def update(self):
		self.age = 30
	def compare(self,other):
		if self.age == other.age:
			return True
		else:
			return False

		
c1 = computer()
c2 = computer()
if c1.compare(c2):
	print("They are same")
else:
	print("They are different")