#Python numpy stacking
#Stacking is of two types : - 1) Horizontal stacking 2) Vertical stacking
import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
print("Performing stacking for 1 dimensional array ")
print("First array is ")
print(arr1)
print("Second array is ")
print(arr2)
print("Now we are performing horizontal stacking ")
print(np.hstack((arr1,arr2)))
print("Now we are performing vertical stacking ")
print(np.vstack((arr1,arr2)))
print("Performing stacking for two dimensional array ")
np.random.seed(122)
arr3 = np.random.randint(1,21,9).reshape(3,3)
arr4 = np.random.randint(31,51,9).reshape(3,3)
print("First array is ")
print(arr3)
print("Second array is ")
print(arr4)
print("Performing horizontal stacking ")
print(np.hstack((arr3,arr4)))
print("Performing vertical stacking ")
print(np.vstack((arr3,arr4)))
