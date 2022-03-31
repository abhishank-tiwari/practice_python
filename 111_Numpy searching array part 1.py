#Numpy searching array
#We can search a value in array and if the required value is found its' index value is returned
import numpy as np
arr = np.array([10,20,30,40,50,40,40])
print("array in which searching to be performed is ")
print(arr)
x = np.where(arr == 40)
print(x)