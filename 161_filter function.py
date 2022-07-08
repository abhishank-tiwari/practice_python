import math
lst = [[1,2,3],[4,5,6],[1,2,3],[3,4]]
new_list = filter(lambda x: sum(x) > 6,lst)
print(list(new_list))