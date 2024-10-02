from functools import reduce

n = int(input())

ks = []

for k in range(n):
    ks.append(int(input()))

curr_left = 0
curr_right = sum(ks)

curr_max = -1
for i in range(len(ks)):
    curr_left += ks[i] ** 2
    curr_right -= ks[i]
    curr_max = max(curr_max,curr_right*curr_left)
    
    
print(curr_max)
