def quickSort(arr, start, finish):
    swap=True
    tSwap=False
    while swap:
        swap=False
        for i in range(start,finish,1):
            if arr[i] > arr[i + 1]:
                t = arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=t
                swap = True
                tSwap=True
    return tSwap

_,k = input().split()
l=list(map(int, input().split()))
c=0
vSwap = True
while vSwap:
    vSwap = False
    for i in range(len(l) - int(k)):
       print(i, i + int(k))
       vSwap = vSwap or bbSort(l, i, i + int(k))
    c += 1
    print()

print(c-1)