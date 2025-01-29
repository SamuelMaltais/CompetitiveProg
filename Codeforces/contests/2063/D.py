def greedy_pick(a,b, k):
    if k == 0:
        return 0
    if len(a) < k or len(b) < k:
        return -1
    if len(a) == 0 or len(b) == 0:
        return -1
    if len(a) < 2 and len(b) < 2:
        return -1

    if len(a) < 2:
        g1 = b.pop()
        g2 = b.pop(0)
        return g2 - g1
    if len(b) < 2:
        g1 = a.pop()
        g2 = a.pop(0)
        return g2 - g1
    
    if a[-1] - a[0] == b[-1] - b[0]:
        a_cpy = a[:]
        return max(greedy_pick()) 


for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    