#Program to count frequency of a number
a = []
size = int(input("Enter size of the list "))
for i in range(size):
	x = int(input(" Enter the number "))
	a.append(x)
count = 0
y = int(input("Enter the number whose frequnecy to be found "))
for i in range(size):
	if a[i] == y:
		count = count + 1
		continue
print("Frequency of ",y," is " , count)