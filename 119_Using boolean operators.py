# Using boolean operators
x = 5
y = 9
command  = True and False == (not x ) and ( not y) or x
print(command)
command = True or False == x and y or ( not x )
print(command)
command = True and True == 1 and 0 or ( not 1 )
print(command)
command = True or False == True and (not False) or ( not True )
print(command)
command = x and y or ( not x ) and ( not y )
print(command)