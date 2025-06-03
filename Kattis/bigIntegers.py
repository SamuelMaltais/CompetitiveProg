for _ in range(int(input())):
    a = input()
    b = input()

    lexiBigger = False
    if a > b:
        lexiBigger = True
    
    actBigger = False
    if len(a) > len(b):
        actBigger = True
    if len(b) == len(a):
        for i in range(len(a)):
            if a[i].isupper() and b[i].islower():
                actBigger = True
                break
            if b[i].isupper() and a[i].islower():
                break
            if a[i] > b[i]:
                actBigger = True
                break
            if a[i] < b[i]:
                break
    
    if lexiBigger and actBigger or (not lexiBigger and not actBigger):
        print('YES')
    else:
        print('NO')