class student:
	com = "LBA"
	def __init__(self,m1,m2,m3):
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3
	def avg(self):
		return (self.m1 + self.m2 + self.m3)/3
	def get_m1(self):
		return self.m1
	def set_m1(self,value):
		self.m1 = value
		return self.m1
	@classmethod
	def info(cls):
		return cls.com
	def data():
		print("This company is LBA")

s1 = student(59,55,56)
s2 = student(66,67,69)
print(s1.avg())
print(s2.avg())
print(s1.info())
print(s2.info())
student.data()
