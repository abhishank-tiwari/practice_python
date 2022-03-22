#List occupies more memory as compared to tuple
import sys
list1 = [1,2,"Ram","Shyam",True,"Ravi"]
tup1 = (1,2,"Ram","Shyam",True,"Ravi")
print("List is ",list1)
print("Size of List",sys.getsizeof(list1))
print("tuple is ",tup1)
print("Size of tuple",sys.getsizeof(tup1))