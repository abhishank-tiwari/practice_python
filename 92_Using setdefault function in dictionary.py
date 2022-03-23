dict1 = {"Brand" : "Maruti" , "Price" : "6 Lac", "Year" : "2022"}
print("Original dictionary is :","\n",dict1)
print("Now using setdefault function")
x = dict1.setdefault("place" , "new delhi")
print("now updated dictionary is ")
print(dict1)