#View vs Copy
#Part 2
import numpy as np
a = np.array([10,20,30,40,50,60])
print("Original array a is (here copy command is used) ","\n",a)
slicing = a[3:6].copy()
print("sliced array named slicing from a is ","\n",slicing)
slicing[:] = 0
print("Assigning 0 to each element of slicing now printing slicing ","\n",slicing)
print("Now printing a after making slicing array(Note changes in a )","\n",a)
print("Conclusion - in copy() changes does not got reflected to original array from which slicing was performed ") 