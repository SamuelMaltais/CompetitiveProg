n = int(input())

accumulated = 0

voyels = 'aeiou'
consonents = ''

for i in range(26):
    if chr(ord('a') + i) not in voyels:
        consonents += chr(ord('a') + i)


triads = []

# deux voyelles
for i in range(len(voyels)):
    for j in range(i + 1, len(voyels)):
        for k in range(len(consonents)):
            triads.append(voyels[i] + voyels[j] + consonents[k])


def tryAll(triads, curr, n):
    global accumulated
    if len(curr) + 3 > 20:
        return
    for triad in triads:
        if accumulated >= n:
            return
        print(curr + triad)
        accumulated += 1
        tryAll(triads, curr + triad, n)
        
tryAll(triads, '', n)