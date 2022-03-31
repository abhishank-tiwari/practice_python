#Searchsorted
#Perform binary search in the array and returns the value where specified value would be inserted to maintain the search order.
import numpy as np
a = np.array([2,5,8,9,10])
x = np.searchsorted(a,7)
#Note . in this method searching is performed from left to right
print(" Index where 7 will be inserted by maintaining serch order ")
print(x)