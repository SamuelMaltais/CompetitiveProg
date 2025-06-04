s=input()
fix = False
if '(' in s:
    o = s.split('(')
    if o[0].count('|') != o[1].count('|'):
        fix = True
    if len(o[1]) != 0:
        if o[1][0] != ')':
            fix = True
    else:
        fix = True
else:
    fix = True

if fix:
    print('fix')
else:
    print('correct')