import math
line=list(map(int, input().split()[1:]))

arrs=[]
def reduce_arr(arr, depth, arrs):
    if len(arr) <= 1:
        return depth
    newarr = []
    for i in range(len(arr) - 1):
        newarr.append(arr[i + 1] - arr[i])
    arrs.append(newarr)
    depth += 1

    if len(newarr) <= 1:
        return depth
    
    if newarr[0] == newarr[1]:
        return depth
    
    else:
        return reduce_arr(newarr, depth, arrs)
    
depth = reduce_arr(line, 0, arrs)


diff = 0
while arrs != []:
    p = arrs.pop()
    diff = p.pop()
    if arrs != []:
        arrs[-1].append(diff + arrs[-1][-1])


print(depth, line[-1] + diff)