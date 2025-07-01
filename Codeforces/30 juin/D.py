import math
for _ in range(int(input())):
    n, m, k = list(map(int, input().split()))
    
    amt = math.ceil(k / n)

    # 1 1 1
    # 0


    rem = m - amt

    if rem == 0:
        print(amt)
    else:
        print(math.ceil(amt / (rem + 1)))


    while True:
        if ((m // a)*(a - 1) + (m % a)) >= amt:
            print(a - 1)
            break
        a += 1

