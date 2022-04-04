# Using filter function to check even or odd
val = [ 5 , 12 , 17 , 18 , 24 , 32 ]
def myFunc(x):
	if x%2 == 0:
		return True
	else:
		return False
even = list(filter( myFunc , val ))
for x in even:
	print(x)

