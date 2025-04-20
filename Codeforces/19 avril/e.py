def nums():
    return list(map(int, input().split()))

for _ in range(int(input())):
    input()
    line = list(input())

    for i in range(len(line)):
        if line[i] == 'P':
            pinks += 1
            if b % 2 == 1:
                cringe += 1
            b = 0
        else:
            c += pinks
            if pinks > 0:
                b += 1   
    
    print(c // 2, cringe)
