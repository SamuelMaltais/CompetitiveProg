import heapq
import random

def nums():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n, m, k = nums()

    qte = (n * m) // k

    
    heap = []
    for i in range(1, k + 1):
        heapq.heappush(heap, (-qte, i))
    
    grid = []
    while len(heap) > 0:
        candidates = []
        for i in range(m):   
            elem = heapq.heappop(heap)
            candidates.append(str(elem[1]))
            if elem[0] < -1:
                heapq.heappush(heap, (elem[0] + 1, elem[1]))

        curr_index = 0
        if len(grid) > 0:
            while curr_index < len(candidates):
                if grid[-1][curr_index] == candidates[curr_index]:
                    random.shuffle(candidates)
                    curr_index = 0
                else:
                    curr_index += 1

        grid.append(candidates)

    for row in grid:
        print(' '.join(row))
