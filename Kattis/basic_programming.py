n, t = map(int, input().split())
arr = list(map(int, input().split()))

if t == 2:
    if arr[0] > arr[1]:
        print('Bigger')
    elif arr[0] == arr[1]:
        print('Equal')
    else:
        print('Smaller')
elif t == 1:
    print(7)
elif t == 3:
    o = arr[:3]
    o.sort()
    print(o[1])
elif t == 4:
    print(sum(arr))
elif t == 5:
    print(sum(map(lambda x: x if x % 2 == 0 else 0, arr)))
elif t == 6:
    s = ''
    for i in arr:
        s += chr(ord('a') + (i % 26))
    print(s)
else:
    visited =  [False for i in range(len(arr))]
    i = 0
    while True:
        i += arr[i]
        if not 0 <= i < len(arr):
            print('Out')
            break
        if visited[i] == True:
            print('Cyclic')
            break
        if i == len(arr) - 1:
            print('Done')
            break
        visited[i] = True
