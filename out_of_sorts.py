line = input().split()

n = int(line[0])
m = int(line[1])
a = int(line[2])
c = int(line[3])
x0 = int(line[4])


arr = []
seen = []

def psudo_bin_search(i, j, list, gt, lt, c):
    
    if j < i:
        return 0
    
    k = (i + j) // 2

    canGoRight = True
    canGoLeft = True


    c += 1

    print(i, j)

    # Can only go right
    if gt > list[k]:
        canGoLeft = False

    # Can only go left
    if lt < list[k] and lt != -1:
        canGoRight = False

    if not (canGoLeft or canGoRight):
        return c

    if canGoLeft:
        c += psudo_bin_search(i, k - 1, list, max(gt, list[k]), min(lt, list[k]), 0)
    if canGoRight:
        if lt == -1:
            lt = list[k]
        c += psudo_bin_search(k + 1, j, list, max(gt, list[k]), min(lt, list[k]), 0)
    
    return c




for _ in range(n):
    x0 = ((a * x0) + c) % m
    arr.append(x0)


print(arr)

print(psudo_bin_search(0, len(arr) - 1, arr, -1, -1, 0))