#Create array by taking input from user
import numpy as np
a = []
size = int(input("Enter size of the array : "))
for i in range(size):
	val = int(input("Enter number "))
	a.append(val)
myarray = np.array(a)
print(myarray)