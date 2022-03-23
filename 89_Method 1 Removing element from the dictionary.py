#Method 1 Removing element from the dictionary
dict1 = { "Model" : "Maruti Alto","Price":"4.5 lac","Year":"2022","color":"black"}
print("Existing dictionary is ")
print(dict1)
print("We want to remove key named Price")
dict1.pop("Price")
print("New updated dictionary is ")
print(dict1)