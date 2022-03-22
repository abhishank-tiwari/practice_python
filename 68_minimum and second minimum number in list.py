#Program to find minimum and second minimum number in list
a = []
size = int(input("Enter size of list "))
for i in range(size):
	x = int(input("Enter number : "))
	a.append(x)
minvalue = min(a)
print("Lowest number is ",minvalue)
a.remove(min(a))
smin = min(a)
print("Second lowest number is ",smin)