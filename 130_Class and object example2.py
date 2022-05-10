class student:
	school = "Telusko"
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
	@classmethod
	def info(cls):
		return cls.school
	@staticmethod
	def mesg():
		print("This is a student class")
		
s1 = student(39,45,47)
s2 = student(97,90,96)
print(s1.avg())
print(s2.avg())
print(s1.get_m1())
print(s2.get_m1())
s1.set_m1(63)
s2.set_m1(77)
print(s1.info())
print(s2.info())
print(student.mesg())