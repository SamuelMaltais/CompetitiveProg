# 
import heapq

for _ in range(int(input())):
    input()

    arr = list(map(int, input().split()))

    c = {}
    for i in arr:
        c[i] = c.get(i, 0) + 1

    arr = list(set(arr))
    heapq.heapify(arr)
    ok = True
    
    #print(arr, c)
    while len(arr) > 0:
        elem = heapq.heappop(arr)

        if c[elem] // 2 >= 1:
            c[elem + 1] = c.get(elem + 1, 0) + c[elem] - 2
            if elem + 1 not in arr:
                    heapq.heappush(arr, elem + 1)
        if c[elem] == 1:
             ok = False
             break
    
    #print(availiable)
    if ok:
        print('YES')
    else:
        print("NO")
                




# 5 -> 6


# 3 3 3 3 3 3 3 4 4 4 4 4 4 4 9 10
# 3 4 5 

# 3 4 5 6 | 3 4 5 6