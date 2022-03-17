#find sum of square of digits of a number
i = int(input("Enter number to find sum of square of digits"))
sum = 0
while(i>0):
	sum = sum + (i%10)*(i%10)
	i = i//10
print("sum of square of digits " , sum)