#The filter function 
#Print ages greater than 18
ages = [ 5,12,17,18,24,32]
def myfunc(x):
	if x < 18:
		return False
	else: 
		return True
		
adults = list(filter(myfunc,ages))

for x in adults:
	print(x)