#Condition selection in python numpy
import numpy as np
arr = np.arange(1,16)
print("Original array arr is ")
print(arr)
print("Checking arr > 10 ")
print(arr > 10)
print(" using b = arr > 10 ")
print(" printing b ")
b = arr > 10
print(b)
print("Using statement arr[b] ")
print(arr[b])
print(" We can directly use arr[arr<5]")
print(arr[arr<5])
print("Printing only even number in this array using arr[arr%2==0] ")
print(arr[arr%2==0])
print("Printing only number equal to 10 in arr using arr[arr==10]")
print(arr[arr==10])
print("Changing all even numbers in array by 0 in arr using arr[arr%2==0] = 0 and then printing arr ")
arr[arr%2==0] = 0
print(arr)