import sys
sys.setrecursionlimit(9999999)

accumulated = 0
voyels = 'aeiou'
consonents = ''

for i in range(26):
    if chr(ord('a') + i) not in voyels:
        consonents += chr(ord('a') + i)

arr = []

def tryAll(curr, i, j):
    global arr
    global accumulated
    if len(curr) == 4:
        arr.append(curr)
        return
    if i > 0:
        for v in voyels:
            tryAll(curr + v, i - 1, j)
    if j > 0:
        for c in consonents:
            tryAll(curr + c, i, j - 1)

tryAll("", 2, 2)

arr = set(arr)

def removeAll(arr):
    toKillList = []
    for k in arr:
        for i in range(26):
            c = chr(ord('a') + i)
            if c + k[1:] in arr and k[0] != c:
                toKillList.append(c + k[1:])
            if k[0] + c + k[2:] in arr and k[1] != c:
                toKillList.append(k[0] + c + k[2:])
            if k[0:2] + c + k[-1] in arr and k[2] != c:
                toKillList.append(k[0:2] + c + k[-1])
            if k[0:3] + c in arr and k[3] != c:
                toKillList.append(k[0:3] + c)
        if len(toKillList) > 0:
            break
    if len(toKillList) > 0:
        for elem in toKillList:
            arr.remove(elem)
        removeAll(arr)
    return
        


removeAll(arr)

print(arr)
print(len(arr))
