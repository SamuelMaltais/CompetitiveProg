a = input()
b = input()

if len(b) > len(a):
    print()
elif a == b:
    print(b.count('1'))
else:
    c = 0
    for i in range(1, len(b)):
        if b[i] == '1':
            break
        c += 1   

    print(max(b.count('1'), len(b) - c + 1))
