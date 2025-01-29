s = input()
r = list(s[::-1])
o = list(s)
ok = False
for i in range(len(o)):
    a = o.pop()
    o.insert(0, a)
    if r == o:
        ok = True
        break

print(int(ok))