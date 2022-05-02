characters = {}
string = "hello world"
for char in string:
	characters[char] = characters.get(char,0) + 1

print(characters)