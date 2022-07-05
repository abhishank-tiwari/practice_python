def sum_items(a = None,b = None ,c = None):
	print(a,b,c)
	return a+b+c

kwargs = { "a" : 5, "b" : 5, "c" : 10}
x = sum_items(**kwargs)
print(x)