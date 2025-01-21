n = int(input())
line = list(map(int, input().split()))
total = sum(line)

stack = []
for i in range(len(line)):
    stack.append((line[i], i + 1))

stack = sorted(stack, key=lambda k: k[0], reverse=True)
moves = []


ok = True
while True:
    if total == 0:
        break

    if total % 2 != 0:
        break
    if stack[0][0] == 0:
        break
    if stack[0][0] == 1 and stack[1][0] == 0:
        ok = False
        break
    if stack[1][0] <= 0:
        ok = False
        break
    
    total -= 2

    stack[0] = (stack[0][0] - 1, stack[0][1])
    stack[1] = (stack[1][0] - 1, stack[1][1])
    moves.append((stack[0][1], stack[1][1]))
    stack = sorted(stack, key=lambda k: k[0], reverse=True)

if ok and total == 0:
    print('yes')
    for move in moves:
        print(move[0], move[1])
else:
    print('no')
