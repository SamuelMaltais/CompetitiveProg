import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

line = input()

q = int(input())

mem = {}

for _ in range(q):
    ints = input().split()
    i = int(ints[0])
    init_i = i
    j = int(ints[1])
    init_j = j

    common = 0
    s = len(line)
    while j < s:
        if i in mem:
            if j in mem[i]:
                common += mem[i][j]
                break
        if line[j] == line[i]:
            common += 1
        else:
            break
        j += 1
        i += 1
    print(common)
    mem[init_i] = {}
    mem[init_i][init_j] = common
