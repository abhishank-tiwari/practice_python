#Python program to check if a string is Palindrome or not
a = input("Enter a string :")
b = a[-1::-1]
if(a==b):
	print("Palindrome string")
else:
	print("Not Palindrome string")