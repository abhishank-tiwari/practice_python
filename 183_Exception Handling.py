a = 5
b = 2
try:
	print("Resource open")
	print(a/b)
	k = int(input("Enter a number : "))
	print(k)

except ZeroDivisionError as e:
	print("Hey,You can not divide a number by Zero",e)
except ValueError as e :
	print("Invalid Input")
except Exception as e:
	print("Something went wrong")
finally:
	print("Resource closed")
