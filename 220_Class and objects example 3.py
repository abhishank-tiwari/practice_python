class Student:
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def average(self):
        return((self.m1+self.m2+self.m3)/3)
    
c1 = Student(55,72,95)
c2 = Student(57,63,52)

a = c1.average()
b = c2.average()

print("First average",a)
print("Second average",b)
