class student():
	def __init__(self,m1,m2,m3):
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3
	def avg(self):
		average = (self.m1 + self.m2 + self.m3)/3
		self.average = average
		return average
	def compare(self,other):
		self.avg()
		other.avg()
		if self.average == other.average:
			print("They have same average")
		elif self.average > other.average:
			print(self,"has greater average than",other)
		else:
			print(other,"has greater average than",self)

			
a1 = student(55,54,53)
a2 = student(66,65,67)
a1.compare(a2)