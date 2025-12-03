import math

def isDup(a):
    for i in range(len(a) // 2):
        if len(a) % (i + 1) != 0:
            continue
        if a[:i + 1] * (len(a) // (i + 1)) == a:
            return True

    return False

l= []
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        l.append(line.strip())

tot = 0
for line in l:
    for ids in line.split(','):
        if '-' not in ids:
            continue
        first, second = ids.split('-')
        first = int(first)
        second = int(second)

        for n in range(first, second + 1):
            if isDup(str(n)):
                tot += n

print(tot)
