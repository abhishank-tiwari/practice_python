#Sum of natural numbers
n = int(input("Enter number upto which you want to sum "))
sum = 0
i = 1
while(i<=n):
	sum = sum + i
	i = i + 1
	
print("Sum is : ",sum)