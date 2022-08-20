class student:
	school = "Abhishank"
	def __init__(self,m1,m2,m3):
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3
	def avg(self):
		return(self.m1 + self.m2 + self.m3)/3
	def getm1(self):
		return self.m1
	def setm1(self,value):
		self.m1 = value
	@classmethod
	def info(cls):
		return cls.school
	@staticmethod
	def information():
		print("This student class is in abc module")

		
s1 = student(34,47,32)
s2 = student(89,32,12)
print(s1.avg())
print(s2.avg())
print(s1.getm1())
print(s2.getm1())
s1.setm1(88)
s2.setm1(98)
print(s1.avg())
print(s2.avg())
student.info()
student.information()