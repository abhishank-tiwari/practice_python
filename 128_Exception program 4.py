a = 5
b = 2
try : 
    print("Resource Open")
    print(a/b)
    k = int(input("Enter a number"))
    print(k)
except ZeroDivisionError as e:
	print("Hey , You can not divide a number by Zero ",e)
except ValueError as e:
	print("Hey ,Wrong Value Input ",e)
except Exception as e:
	print("Hey ,Something went wrong ",e)
finally:
    print("Resource closed")
print("Bye")
