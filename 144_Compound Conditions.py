#Compound condition
#True and True = True 
#True and False = False
#False and False = False
#True or True = True
#True or False = True
#False or False = False

x = 2
y = 4
compound = x < y and y + 2 > 3
print(compound)
compound = True and True
print(compound)
compound = True and False
print(compound)
compound = True or True
print(compound)
compound = False or True
print(compound)
compound = False or False
print(compound)
compound = False and False
print(compound)
x = 2
y = 4
compound  = x > y or y + 2 > 3
print(compound)
compound = x>y and y+2>3 and False
print(compound)
compound = x>y or y+2>3 and 2 == 3
print(compound)
compound = not(x<y)
print(compound) 
compound = not(x<y and 1 == 1)
print(compound)
compound = not False == False
print(compound) 
compound = 1 == ( not 1)
print(compound)
compound = not True == False
print(compound)
#Conditional/Comparison operators
#Not
#and 
#or
compound = True or False and not True or False
print(compound)
compound = not(True or False) and not False or 2 < 3 or True 
print(compound)
#Demorgan's Law
# not(x and y) == (not x) or (not y)
# not(x or y) == (not x) and (not y)
cond = not ( 1 and 0 ) == (not 1) or (not 0)
print(cond)
