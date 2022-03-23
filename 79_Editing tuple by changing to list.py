#Tuple are immutable it means they can not be changed
#But you can convert tuple to list and then make changes in a list and convert it into tuple
#Example
y = ("amitabh","akshay","shahrukh","salman")
print("tuple y is ",y)
print("Converting tuple y to list z ")
z = list(y)
print("assigning z[0] = tom cruise")
z[0]= "tom cruise"
print("Edited list z is :",z)
print("converting list z to tuple y")
y = tuple(z)
print("Edited tuple y is ",y)