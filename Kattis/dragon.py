line = input().split()

n = int(line[0])
k = int(line[1])

line = input().split()
i = 0
student = 0
stack = []

while i < len(line):

    command = line[i]
    if command == 'undo':
        num = int(line[i + 1])
        for _ in range(num):
            if(len(stack) > 0):
                student -= stack.pop()
        i += 1
    else:
        num = int(command)
        student += num
        stack.append(num)

    i += 1

ok = student % n
if ok >= 0:
    print(ok)
else:
    print(n - ok)