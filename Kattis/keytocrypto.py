l=input()
s=input()

ori=''
for i in range(len(l)):
    shift = ''
    if i < len(s):
        shift = s[i]
    else:
        shift = ori[i - len(s)]

    change = ord(shift) - ord('A')
    new = ord(l[i]) - change
    if new < ord('A'):
        new = new + 26
    ori += chr(new)

print(ori)