stack = []

# on sen fout du length
input()
line = input()

i = 0
is_ok = True
broke = ''

for c in line:
    if c == ' ':
        pass
    elif c in ['(','[','{']:
        stack.append(c)
    else:
        if(len(stack) == 0):
            is_ok = False
            broke = c
            break
        to_close = stack.pop()
        opposite = ''
        if to_close == '(':
            opposite = ')'
        elif to_close == '[':
            opposite = ']'
        else:
            opposite = '}'
        

        if c != opposite:
            is_ok = False
            broke = c
            break

    i += 1


if is_ok:
    print("ok so far")
else:
    print(broke + " " + str(i))