l= []

with open('input2.txt') as f:
    lines = f.readlines()
    for line in lines:
        l.append(line.strip())

tot = 0

columns = []
ops = []
for line in l:
    if '*' in line:
        ops = line.split(' ')
    else:
        columns.append(list(map(int, line.split())))

for i in reversed(range(len(ops))):
    if ops[i] == '':
        ops.pop(i)

print(ops, columns)

for i in range(len(ops)):
    curr = int(ops[i] == "*")
    o = ops[i]


    numbers = []
    for col in columns:
        numbers.append(col[i])
    
    m = max(numbers)
    fill = len(str(m))

    fixed = []

    for n in numbers:
        f = list(str(n))
        while len(f) < fill:
            f.insert(0, -1)
        fixed.append(f)

    for i in range(len(fixed)):
        toAdd = ""
        for f in fixed:
            if f[i] != '-1' and f[i] != -1:
                toAdd += str(f[i])
        if o == "*":
            curr *= int(toAdd)
        else:
            curr += int(toAdd)
        print(toAdd)
    print()
    tot += curr

print(tot)
