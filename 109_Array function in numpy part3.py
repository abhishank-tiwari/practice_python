# Array function numpy Part 3
import numpy as np
np.random.seed(122)
arr = np.random.randint(1,21,10)
print("Printing the original array ")
print(arr)
print(" Now shuffling all the elements ")
np.random.shuffle(arr)
print(arr)
print(" Lets display unique elements of array ")
print(np.unique(arr)) 
print("Lets count unique count of elements ")
print(np.unique(arr).size)