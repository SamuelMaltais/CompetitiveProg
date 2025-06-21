for _ in range(int(input())):
    n,m = list(map(int, input().split()))
    if m < n:
        print(-1)
        continue

    if m > ((n + 1)*n)/2:
        print(-1)
        continue

    ini_n = n
    seq = []
    present = set()
    while True:
        diff = (m - n) + 1
        if diff > n:
            m -= n
            seq.append(n)
            n -= 1
        elif diff != 1:
            seq.append(diff)
            n = m
        else:
            seq.append(1)
            break

    print(seq[0])
    for i in range(len(seq) - 1):
        print(seq[i], seq[i + 1])
        present.add(seq[i])
    
    present.add(1)
    prev = 1
    for i in range(1,ini_n+1):
        if i not in present:
            print(prev, i)
            prev = i


    