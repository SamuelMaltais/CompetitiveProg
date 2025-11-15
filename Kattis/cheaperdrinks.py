from random import randint

n=int(input())

l = []


def compare(a, b):
    if len(a) == len(b):
        if a < b:
            return 1
        elif a == b:
            return 2
        else:
            return 0


    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            res = a[i] >= b[i] 
            return int(res)
        
    if len(a) > len(b):
        i = len(b)
        print(a, b)
        while i < len(a):
            if b[-1] != a[i]:
                res = b[-1] >= a[i] 
                return int(res)

    i = len(a)
    while i < len(b):
        if a[-1] != b[i]:
            res = a[-1] >= b[i] 
            return int(res)

    return 2


# STOLEN BECAUSE I HAVE NO TIME, LOL
def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        c = compare(item, pivot)
        if c == 0:
            low.append(item)
        elif c == 2:
            same.append(item)
        elif c == 1:
            high.append(item)

    return quicksort(low) + same + quicksort(high)

for _ in range(n):
    i = input()
    canSwap=True
    for c in i:
        if c not in ['8','9','6','1','0']:
            canSwap = False
            break
    if canSwap:
        new=""
        for j in reversed(range(len(i))):
            # XD
            if i[j] == '6':
                new += '9'
            elif i[j] == '9':
                new += '6'
            else:
                new += i[j]
        
        if i < new:
            l.append(i)
        else:
            l.append(new)

    else:
        l.append(i)
    

l = quicksort(l)
#print(l)
print("".join(l))