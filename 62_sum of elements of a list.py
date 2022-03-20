#Program to find sum of elements of a list
a = []
val = int(input(" How many elements you want to enter in the list"))
for i in range(val):
	x = input("Enter val")
	a.append(x)
sum = 0
for j in range(val):
	sum = sum + int(a[j])
print("sum of elements in ",a ," is " , sum)