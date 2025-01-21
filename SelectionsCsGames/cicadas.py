earliest_year = 99999999
for _ in range(int(input())):
    line = list(map(int, input().split()))
    start, c1, c2 = line
    curr = max(c1,c2)
    while True:
        if curr % c1 == 0 and curr % c2 ==0:
            break
        curr += 1
    earliest_year = min(curr + start, earliest_year)
print(earliest_year)