a = int(input("Enter marks in first subject"))
b = int(input("Enter marks in second subject"))
c = int(input("Enter marks in third subject"))
d = int(input("Enter marks in fourth subject"))
e = int(input("Enter marks in fifth subject"))
t= ((a + b + c+ d + e)*100)/500

if t>=80:
    print("Grade is A")
elif t>=60 and t<80:
    print("Grade is B")
elif t>=50 and t<60:
    print("Grade is C")
elif t>= 35 and t<50:
    print("Grade is D")
else:
    print("Grade is E")