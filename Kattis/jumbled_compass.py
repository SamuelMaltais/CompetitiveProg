a = int(input())
b = int(input())

right = None
left = None

if a > b:
    left = a - b
    right = (360 - a) + b
else:
    left = a + 360 - b
    right = b - a

if right < left:
    print(right)
elif right == left:
    print(abs(right))
else:
    print(-left)
