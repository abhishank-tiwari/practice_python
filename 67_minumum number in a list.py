#Program to find minumum number in a list
a = []
size = int(input("Enter size of a list "))
for i in range(size):
	y = int(input("Enter the number "))
	a.append(y)
min = a[0]
for i in range(size):
	if min>a[i]:
		min = a[i]

print("Minimum number in ",a," is ",min)