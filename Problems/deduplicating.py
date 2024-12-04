def hash(s):
    f = True
    total = 0
    for char in s:
        if f:
            total = ord(char)
            f = False
        else:
            total = total ^ ord(char)

    return total

def calc(n):
   return (n*(n - 1)) / 2

while True:
    n = int(input())
    if n == 0:
        break
    d = {}
    s = {}

    d2 = {}
    for n in range(n):
        i = input()
        h = hash(i)
        if h in d:
            d[h] += 1
            if i in d2[h]:
                d2[h][i] += 1
            else:
                d2[h][i] = 1
        else:
            d[h] = 1
            d2[h] = {}
            d2[h][i] = 1

        if i not in s:
            s[i] = 1
        

        


    collisions = 0
    for key in d:
        n = 0
        groups = []
        for k in d2[key]:
            if d2[key][k] == 1:
                n += 1
            else:
                groups.append(d2[key][k])

        fac2 = 0
        for i in groups:
            fac2 += i * n

        for i in range(len(groups)):
            for j in range(i + 1, len(groups)):
                fac2 += groups[i] * groups[j]

        if(d[key] > 1):
            collisions += calc(n) + fac2

    unique = 0
    for key in s:
        unique += 1

    print(str(unique) + " " + str(int(collisions)))