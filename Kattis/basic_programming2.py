import math

n, t = list(map(int, input().split()))
arr = list(map(int, input().split()))

def f():
    m = set()
    if t == 1:
        for elem in arr:
            if 7777 - elem in m:
                print('Yes')
                return
            m.add(elem)
        print('No')
    elif t == 2:
        for elem in arr:
            if elem in m:
                print('Contains duplicate')
                return
            m.add(elem)
        print('Unique')
    elif t == 3:
        m = {}
        for elem in arr:
            m[elem] = dict.get(m, elem, 0) + 1
            if m[elem] > len(arr) / 2:
                print(elem)
                return
        print(-1)
    elif t == 4:
        arr.sort()
        if len(arr) % 2 == 0:
            print(arr[(len(arr) // 2) - 1], arr[len(arr) // 2])
        else:
            print(arr[len(arr) // 2])
    else:
        arr.sort()
        arr2 = []
        for e in arr:
            if 100 <= e <= 999:
                arr2.append(str(e))
        print(' '.join(arr2))
f()