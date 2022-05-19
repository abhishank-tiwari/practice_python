words = ("abhishank","Priya","shashank","Prashant")
target = "abhishank"
found = False
for word in words:
	if word == target:
		print("I found the word!")
		found = True
	if not found:
		print("I didn't found the word")	