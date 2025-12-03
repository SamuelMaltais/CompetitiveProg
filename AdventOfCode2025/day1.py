import math

l= []
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        l.append(line.strip())

curr = 50
tot = 0
val = 50

for line in l:
    n = 0
    
    if line[0] ==  'R':
        n = int(line[1:])
    else:
        n = -int(line[1:])


    cycles = math.floor(abs(n) / 100)
    rem = (abs(n) % 100) * (1 if n >= 0 else -1)
    
    was_zero = (val == 0)
    tot += abs(cycles)

    val += rem
    if val < 0:
        val += 100
        if not was_zero:
            tot += 1
        if val == 0:
            tot -= 1
    if val > 99:
        val -= 100
        if not was_zero:
            tot += 1
        if val == 0:
            tot -= 1
    if val == 0:
        tot += 1
    #print(val, tot, cycles, rem)
print(tot)