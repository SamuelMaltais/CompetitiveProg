import math
import sys

sys.setrecursionlimit(999999999)


s=0
arr=input()
n = len(arr)

def count_right(initial_number, curr_index, arr):
    if last_seen[int(initial_number)] != -1:
        return curr_index - last_seen[int(initial_number)]
    else:
        return curr_index + 1

def count_right2(initial_number, curr_index, arr, last_seen):
    if last_seen[int(initial_number)] != -1:
        return last_seen[int(initial_number)] - curr_index
    else:
        return curr_index + 1

def count_left(initial_number, curr_index, arr, last_seen):
    if last_seen[int(initial_number)] != -1:
        return curr_index - last_seen[int(initial_number)]
    else:
        return curr_index + 1
    
def set_seen(last_seen, num, i):
    num = int(num)
    while num >= 0:
        last_seen[int(num)] = i
        num -= 1

last_seen = [-1 for _ in range(10)]

counts = [(0,0) for _ in range(len(arr))]

for c in range(len(arr)):
    counts[c] = (count_left(arr[c], c - 1, arr, last_seen),0)
    right = count_right(arr[c], c + 1, arr)
    set_seen(last_seen, arr[c], c)
    

for c in counts:
    left = c[0]
    right = c[1]
    total = left*right + left + right + 1
    s += total*int(arr[c])

d = n*(n+1)/2
diviseur = math.gcd(int(s), int(d))

s = s // diviseur
d = d // diviseur
s = int(s)
d = int(d)

if d != 0:
    if s % d == 0:
            print(s // d)
    else:
        if s > d:
            print(s // d, str(s % d) + '/' + str(d))
        else:
            print(str(s) + '/' + str(d))
else:
    print(0)