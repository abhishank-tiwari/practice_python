#Print numbers divisible by 5 using continue
nums = { 12 , 16 , 15 , 21 , 26 }
for num in nums :
	if num%5 == 0:
		print(num)
		continue      
else:
	print("not found")