input()

def dp(arr, mem, player):
    ok = tuple(arr)
    if ok in mem:
        return
    
    res=0    
    if len(arr) == 1:
        if arr[0] % 2 == 1:
            res=1*player

    elif len(arr)!=0:

        path1Arr = arr[1:]
        path2Arr = arr[:-1]

        dp(path1Arr, mem, -player)
        dp(path2Arr, mem, -player)

        path1 = mem[tuple(path1Arr)] + (arr[0] % 2) * player
        path2 = mem[tuple(path2Arr)] + (arr[-1] % 2) * player

        if player  == -1:
            res = min(path1, path2)
        else:
            res = max(path1, path2)

    mem[ok] = res
        
mem = {}
c=0

arr=list(map(int, input().split()))

for i in range(len(arr)):
    t = arr.pop()

    dp(arr, mem, -1) 
    if mem[tuple(arr)] + t % 2 > 0:
        c += 1
    
    # Rotation pas smart du array
    arr.append(t)
    t=arr.pop(0)
    arr.append(t)

print(c)