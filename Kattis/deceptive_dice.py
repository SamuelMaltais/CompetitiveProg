import math
def dice_expentency(k, n):
    if k == 1:
        return (n+1)/2

    next_expentency = dice_expentency(k-1, n)
    cut = 0
    for i in range(math.ceil(next_expentency), n + 1):
        cut += i
    cut /= (n - math.ceil(next_expentency) + 1)
    odds = (n - math.ceil(next_expentency) + 1) / n
    return odds*cut + (1-odds)*next_expentency


n, k = input().split()
n = int(n)
k = int(k)
print(dice_expentency(k, n))

# print(dice_expentency(k, n))