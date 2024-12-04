import math
l = input().split()

p = int(l[0])
a = int(l[1])
b = int(l[2])
c = int(l[3])
d = int(l[4])

n = int(l[5])

def price(k):
    return p*(math.sin(a*k + b) + math.cos(c*k + d) + 2)

best_decline = 0
curr_max = 0

for i in range(1, n + 1):
    prix = price(i)
    if prix >= curr_max:
        curr_max = prix
    else:
        best_decline = max(best_decline, curr_max - prix)


print(best_decline)