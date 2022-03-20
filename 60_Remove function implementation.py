a = []
for i in range(5):
	x = input("Enter value")
	a.append(x)
print("original list is ",a)
val = input("Enter the value to remove")
a.remove(val)
print("List after deletion",a)