lst = [ 5,1 , 2 ,3 ,-2]
i = 0
result = 0
while i< len(lst):
	num = lst[i]
	result = num + result
	i += 1

print(result)