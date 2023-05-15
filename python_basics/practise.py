
lst = [1,2,3,4,5,6,7,8,9,10,11,12]

# #Filter
# f = filter(lambda x:x*5==0, lst)
# print(list(f))

# #MAp
# print("MAPS")
# m = map(lambda x:x+y, lst)
# print(list(m))

#Reduce
from functools import reduce
print("REDUCE")
m = reduce(lambda x:x+5, lst)
print(m)