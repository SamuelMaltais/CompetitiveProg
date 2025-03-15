for i in range(int(input())):
    a,b,c = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    a1 = min(arr)

    m={}
    for elem in arr:
        m[elem] = dict.get(m, elem, 0) + 1

    flag = True
    for i in range(a):
        for j in range(a):
            if not (a1 + b*j + c*i) in m:
                flag = False
                break
            else:
                m[(a1 + b*j + c*i)] -= 1
                if m[(a1 + b*j + c*i)] < 0:
                    flag = False
                    break
    if flag:
        print('YES')
    else:
        print('NO')