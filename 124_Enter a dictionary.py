counts = {}
while True:
	num = input(" Number ( Enter q to quit ) ")
	if num == "q":
		break
	num = int(num)
	counts[num] = counts.get(num,0) + 1
    
print(counts)