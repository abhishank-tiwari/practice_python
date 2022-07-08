import math
lst = [[1,2,3],[4,5,6],[1,4,3],[3,4]]
new_list = filter(lambda y: y%2 == 0, map(lambda x: sum(x),lst))
print(list(new_list))