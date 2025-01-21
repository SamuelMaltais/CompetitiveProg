for _ in range(int(input())):
    input()
    arr = list(map(int,input().split()))
    i=0
    curr=arr[i]
    while True:
        if arr[i] < curr:
            while i >= 0 and 