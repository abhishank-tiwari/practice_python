import re

line = "python and Java gives Jython"

r1 = re.match(r'Java',line)

print("On failure :",r1)

r2 = re.match(r'python' , line)

print("On Success :",r2)