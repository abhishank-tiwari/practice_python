#Write a program to search a number in the list
a = []
size = int(input("Enter size of the list "))
for i in range(size):
	val = int(input("Enter the number "))
	a.append(val)
key = int(input("Enter number to be searched "))
flag = 0
for i in range(size):
	if(a[i] == key):
		flag = 1
		pos = i + 1
		break
if(flag == 1):
		print("Element found at position ",pos)
else:
		print("Element not found")		
