for _ in range(int(input())):
    
    x, y = input().split()
    x = int(x)
    y = int(y)

    if x == y:
        print("NO")
    elif x + 1 == y:
        print("YES")
    elif x + 1 < y:
        print('NO')
    else:

        # 209 210 -> 11 3

        diff = (x - y + 1)

        if diff % 9 == 0:
            print("YES")
        else:
            print("NO")