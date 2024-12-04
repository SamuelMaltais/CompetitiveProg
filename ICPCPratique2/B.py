import math

n = input()

line = input().split()

elems = []

for elem in line:
    elems.append(-int(elem))

elems.sort()

euh = int(math.ceil(len(elems) / 2) - 1)

votes = 0

for i in range(euh):
    votes += (-elems[i])


for i in range(euh, len(elems)):
    votes += int(math.ceil((-elems[i]) / 2) - 1)

print(votes)