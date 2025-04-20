def nums():
    return list(map(int, input().split()))


import heapq

for _ in range(int(input())):
    n, k = input().split()
    k = int(k)

    l = nums()
    r = nums()

    worst = 0
    prio_q = []

    for i in range(len(l)):
        if l[i] > r[i]:
            heapq.heappush(prio_q, -r[i])
            worst += l[i]
        else:
            heapq.heappush(prio_q, -l[i])
            worst += r[i]

    rem = 1

    for i in range(k - 1):
        rem += -heapq.heappop(prio_q)

    print(worst + rem)