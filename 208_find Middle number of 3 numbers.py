a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))
if (a>b and a<c) or (a>c and a<b):
    print("Middle number is : ",a)
elif(b>a and b<c) or(b>c or b<a):
    print("Middle number is :",b)
else:
    print("Middle number is :",c)