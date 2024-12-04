import sys
import heapq
input = sys.stdin.readline

line = input().split()
c = int(line[2])
h = int(line[1])
n = int(line[0])

stack = []

for _ in range(n):
    line = input().split()
    curr_heap = []
    for s in line:
        heapq.heappush(curr_heap, int(s))
    stack.append(curr_heap)
    

flag = True
candles = 0
while flag:
    if(len(stack) == 0):
        break
    if(len(stack[0]) == 0):
        break
    stack.sort(key=lambda x: x[0])
    for i in range(len(stack)):
        if len(stack[i]) != 0:
            c -= heapq.heappop(stack[i])
        if c < 0:
            flag = False
            break
        candles += 1
    
print(candles)
