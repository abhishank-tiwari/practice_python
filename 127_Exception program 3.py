a = 5
b = 2
try : 
    print("Resource Open")
    print(a/b)
except Exception as e:
	print("Hey , You can not divide a number by Zero ",e)
finally:
    print("Resource closed")
print("Bye")
