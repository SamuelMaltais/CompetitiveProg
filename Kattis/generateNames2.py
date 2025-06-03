accumulated = 0
voyels = 'aeiou'
consonents = ''

print(25248)

for i in range(26):
    if chr(ord('a') + i) not in voyels:
        consonents += chr(ord('a') + i)

arr = []

def tryAll(curr, i, j):
    global arr
    global accumulated
    if len(curr) == 3:
        if i > 0:
            f = ''
            for v in voyels:
                if v not in curr:
                    f = v
                    break
            accumulated += 1
            arr.append(f + curr)
            # arr.append(curr[0] + f + curr[1:])
            # arr.append(curr[0:2] + f + curr[-1])
            # arr.append(curr[0:3] + f)
            return
        else:
            f = ''
            for c in consonents:
                if c not in curr:
                    f = c
                    break
            arr.append(f + curr)
            # arr.append(curr[0] + f + curr[1:])
            # arr.append(curr[0:2] + f + curr[-1])
            # arr.append(curr[0:3] + f)
            return

    if i > 0:
        for v in voyels:
            tryAll(curr + v, i - 1, j)
    if j > 0:
        for c in consonents:
            tryAll(curr + c, i, j - 1)

tryAll("", 2, 2)
arr = set(arr)

for elem in arr:
    print(elem)
print(len(arr))