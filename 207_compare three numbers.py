a = int(input("Enter first number "))
b = int(input("Enter second number "))
c = int(input("Enter third number"))
if a>b and a>c:
	print("max number is ",a)
elif b>a and b>c:
	print("Max number is ",b)
else:
	print("Max number is ",c)