#Index function implementation in python
a = []
for i in range(5):
	x = input("Enter Value :")
	a.append(x)
x = input("Enter the value to find index :")
z = a.index(x)
print("Index = ",z)