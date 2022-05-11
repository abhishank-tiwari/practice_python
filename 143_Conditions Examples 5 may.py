#Program on Conditions
cond = 2 == 3
print(cond)
cond = 3.0 == 3
print(cond)
x = 4
y = 4
cond = x == y
print(cond)
cond = x < 5
print(cond)
cond = x + 5 > 5
print(cond)
cond = x + 6 == 19
print(cond)
str1 = "hello"
str2 = "Hello"
cond = str1 == str2
print(cond)
str1 = "ab"
str2 = "ac"
cond = str1 > str2
print(cond)
cond = str1 < str2
print(cond) #ASCII Codes are used to compare strings
# ASCII code of a is 097 , b is 098 .... z is 122
# ASCII code of A is 065 , B is 066 .... Z is 090
# ASCII value of a String is the Sum of ASCII values of all characters of a String
#To get ASCII Code of a alphabet ord() function is used
print(ord("a"))
print(ord("A"))
#To print an alphabet as per its ASCII value chr() function is used
print(chr(99))
cond = True == 1
print(cond)
cond = False == 0
print(cond)
cond = True == "True"
print(cond)