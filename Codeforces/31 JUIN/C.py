for _ in range(int(input())):
    n=input()    
    p = list(map(int, input().split()))

    s = []

    currMin = float('infinity')
    for e in p:
        currMin = min(e, currMin)
        if e == currMin:
            s.append('1')
        else:
            s.append('0')

    currMax = float('-infinity')
    for i in reversed(range(len(p))):
        e = p[i]
        currMax = max(currMax,e)
        if e == currMax:
            s[i] = '1'

    print(''.join(s))
