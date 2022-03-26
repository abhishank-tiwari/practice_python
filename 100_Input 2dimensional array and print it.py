#Input 2dimensional array and print it
import numpy as np
matrix = []
row = int(input("Enter number of rows "))
col = int(input("Enter number of columns "))
for i in range(row):
	a = []
	for j in range(col):
		val = int(input("Enter number :"))
		a.append(val)
	matrix.append(a)
arr = np.array(matrix)
for i in range(row):
	for j in range(col):
		print(arr[i][j],end = " ")
	print()