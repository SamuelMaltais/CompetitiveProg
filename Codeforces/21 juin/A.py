from copy import deepcopy

# def backtrack(length, height, rects):
#     if len(rects) == 0:
#         if length == height:
#             return True
#         return False
    
#     t = rects.pop()

#     cp = deepcopy(rects)
#     cp2 = deepcopy(rects)

#     res1 = backtrack(length + t[0], height + t[1], cp)
#     res2 = backtrack(length + t[1], height + t[0], cp2)
    
    
#     return res1 or res2    


def fill_rect(rects):
    rects.sort(reverse=True)
    m=-1
    for r in rects:
        m = max(m, r[0])

    curr_height = 0
    i=0
    taken = 0
    while i < len(rects):
        r = rects[i]
        if r[0] == m:
            curr_height += r[1]
            taken += 1
        else:
            if i + 1 < len(rects):
                if rects[i + 1][0] + r[0] == m and rects[i + 1][1] == r[1]:
                    curr_height += r[1]
                    i += 1
                    taken += 2
        i += 1

    return (curr_height == m) and taken == 3

for _ in range(int(input())):
    l1,b1,l2,b2,l3,b3 = list(map(int, input().split()))


    # Base as the longuest element
    base = max(b1, b2, b3)
    curr_height = 0
    availiable = [(l1,b1),(l2,b2),(l3,b3)]
    availiable2 = [(b1,l1),(b2,l2),(b3,l3)]

    
    if fill_rect(availiable2) or fill_rect(availiable):
        print("YES")
    else:
        print("NO")