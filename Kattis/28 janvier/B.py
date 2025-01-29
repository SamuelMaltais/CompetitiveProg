s=input()

id = input()

r = ''
for i in range(0, len(id), 3):
    r += s[int(id[i: i + 3]) - 1]
print(r)