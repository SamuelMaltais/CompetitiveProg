for _ in range(int(input())):
    n = int(input())


    counts = {
        0: 0,
        1: 0,
        2: 0,
        3: 0
    }

    for i in range(n):
        counts[i % 4] += 1
    
    a=False
    if counts[0] != counts[3]:
        a = True
    elif counts[1] != counts[2]:
        a = True

    # a = True
    # for i in range(n):
    #     r = (i - 3) % 4
    #     if r <= n and r != i:
    #         a = False
    #         break

    # ((a + b) - 3) % 4 = 0
    
    
    if a:
        print("Alice")
    else:
        print("Bob")