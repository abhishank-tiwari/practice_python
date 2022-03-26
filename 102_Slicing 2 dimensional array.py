#Slicing 2 dimensional array 
import numpy as np
np.random.seed(111)
a = np.random.randint(1,500,30).reshape(6,5)
print("Orifginal array is : " ,"\n" ,a)
print(" Performing slicing as a[:3,0:3] ")
print(a[:3,0:3])