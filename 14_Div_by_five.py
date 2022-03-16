#Print numbers divisible by 5 using break
nums = { 12 , 16 , 15 , 21 , 26 }
for num in nums :
	if num%5 == 0:
		print(num)
		break          
else:
	print("not found")