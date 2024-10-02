line = input().split()
G = int(line[0])
T = int(line[1])
N = int(line[2])

maxVal = 0.9 * (G - T)


items = input().split()
l = []
for i in items:
    maxVal -= int(i)

print(int(maxVal))

