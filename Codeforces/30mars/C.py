for _ in range(int(input())):
    input()
    l = list(map(int, input().split()))
    pair = []
    impair = []
    for elem in l:
        if elem % 2 == 0:
            pair.append(elem)
        else:
            impair.append(elem)
    
    if len(pair) == 0:
        print(max(impair))
        continue
    if len(impair) == 0:
        print(max(pair))
        continue

    option1 = sum(pair) + max(impair)
    option2 = sum(impair) + max(pair)

    print(max(option1,option2))
