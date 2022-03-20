#program to find total number of odd and even number in a list
a = []
size = int(input("total number of elements in the list"))
for i in range(size):
	x = int(input("Enter the number : "))
	a.append(x)
co =0
ce = 0
for i in range(size):
	if a[i]%2 == 0:
		ce = ce + 1
	elif a[i]%2 != 0:
		co = co + 1

print("number of odd in list ",a," is ",co)
print("number of even in list ",a," is ",ce)