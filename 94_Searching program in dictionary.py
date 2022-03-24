#Searching Program in Dictionary
students_DB = {}
#ask input from user or q to exit
while True:
	line = input("Please input ID name and name sepearted by comma or q to exit : ")
	if line == "q":
		break 
	id,name = line.split(' , ')
	students_DB.update({id:name})
#output
for x,y in students_DB.items():
	print(x,y)
	
#Searching a key
key = input("Enter an id to be searched ")
	
if key in students_DB:
	print("ID = ",key,"Student's name = ",students_DB[key])
else:
	print("Students id not found")