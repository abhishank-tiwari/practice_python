#Program to implement count method
a = []
for i in range(10):
	x = input("Enter item to add in the list :")
	a.append(x)
x = input("Enter value whose frequency you want :")
f = a.count(x)
print("Frequency of " , x,"is " , f) 