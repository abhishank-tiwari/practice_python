#Pop function
#To delete last element from the list
#syntax : list.pop()
a = []
for i in range(5):
	x = input("Enter value")
	a.append(x)
print("Entered list is " , a )
print("Now applying pop function ")
a.pop()
print("List after applying pop function",a)