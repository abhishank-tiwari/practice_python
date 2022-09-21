from array import *
arr = array("i",[])
n = int(input("Enter length of array"))
for i in range(n):
	x = int(input("Enter the next value"))
	arr.append(x)

print("Array is ",arr)
s = int(input("Enter the value to be searched"))
c = 0
for i in arr:
	if s == i:
		print("index is ",c)
	c = c + 1
