#List takes more time to execute as compared to tuples
import timeit
listtime = timeit.timeit(stmt = "[1,2,3,4,5,6]",number = 6000000)
tupletime = timeit.timeit(stmt = "(1,2,3,4,5,6)",number = 6000000)
print("List takes time :",listtime)
print("Tuple take time :",tupletime)