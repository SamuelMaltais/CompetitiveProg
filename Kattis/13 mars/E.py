n = int(input())

maxones = n // 2
s = list('1' * maxones)

if  n % 2 == 1:
    s[0] = '7'

print("".join(s))

