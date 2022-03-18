#Enter number upto which you want to find sum of squares 
n = int(input("Enter number upto which you want to sum squares"))
sum = 0
i = 1
while(i<=n):
	sum = sum + i*i
	i = i + 1
print("Sum of squares is : ",sum) 