#Numpy searching array
#If we want to get all the indexes where there are even numbers
import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10])
result = np.where(a%2 == 0)
print("Indexes where there are even numbers ","\n",result)