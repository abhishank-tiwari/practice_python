#Sum function with multiple arguments
def sum(a,*b):
	c = a
	for i in b:
		c = c + i
	print(c)

sum(5,9,7,8,31,41)