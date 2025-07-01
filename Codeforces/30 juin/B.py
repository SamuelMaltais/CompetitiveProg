for _ in range(int(input())):
    n, s = input().split()
    s = int(s)
    line = list(map(int, input().split()))

    line.sort()

    teams = 0
    first = True
    minStrength = 0
    count = 1
 
    for t in reversed(line):
        if first:
            first = False
            minStrength = t
            count = 1
        else:
            count += 1
            minStrength = min(minStrength, t)
        if minStrength*count >= s:
            teams += 1
            first = True
    
    print(teams)
        