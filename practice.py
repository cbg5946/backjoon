import copy
res = [1,2,3,4]
origin = copy.deepcopy(res)
res.pop()

print(origin)