for _ in range(int(input())):
    input()
    
    expected = {
        0: 3,
        1: 1,
        3: 1,
        2: 2,
        5: 1
    }
    needed = 8

    line = input().split()
    ok = False
    for i in range(len(line)):
        d = int(line[i])
        if d in expected:
            if expected[d] > 0:
                expected[d] -= 1
                needed -= 1
        if needed == 0:
            print(i + 1)
            ok = True
            break

    if not ok:
        print(0)
    

