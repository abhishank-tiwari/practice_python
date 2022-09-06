def AreaCir(r):
	PI = 3.14
	area = PI*r*r
	return area
	
y = float(input("Enter radius of circle whose area to find : "))
z = AreaCir(y)
print("Area of circle is : ",z)
