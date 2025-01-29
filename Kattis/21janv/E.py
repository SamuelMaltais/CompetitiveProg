while True:
    a, b = input().split()
    if a == '0' and b == '0':
        break
    a = list(reversed(a))
    b = list(reversed(b))
    op = 0
    for i in range(max(len(a), len(b)) + 1):
        if i >= len(a):
            a.append('0')
        if i >= len(b):
            b.append('0')
        c = int(a[i]) + int(b[i])
        if c > 9:
            op += 1
            if i + 1 < len(a):
                a[i + 1] = str(int(a[i+1]) + 1)
            else:
                a.append(1)
    if op == 0:
        print('No carry operation.')
    elif op ==1:
        print(str(op) + " carry operation.")
    else:
        print(str(op) + " carry operations.")