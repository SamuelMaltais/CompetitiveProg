import math

l= []

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        l.append(list(line.strip()))

tot = 0

def findFrom(i, line, val):
    while i < len(line):
        if line[i] == val:
            return i
        i += 1

    return -1

def formRes(i, line, curr):
    if len(curr) == 12:
        return ""

    for val in reversed(range(1, 10)):
        if str(val) in line:
            v = findFrom(i, line, str(val))
            if v != -1 and len(line) - v + len(curr) >= 12:    
                return line[v] + formRes(v + 1, line,line[v] + curr)
    
for line in l:
    res = formRes(0, line, "")
    tot += int(res)

print(tot)