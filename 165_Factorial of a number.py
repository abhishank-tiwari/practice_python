def fact(n):
	f = 1
	for i in range(1,n+1):
		f = f*i
        i = i + 1
	return f

print ("Factorial of 5")
print(fact(5))