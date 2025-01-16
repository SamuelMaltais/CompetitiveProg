input()
c=1
ok = True
for elem in input().split():
    if elem != 'mumble':
        if int(elem) != c:
            ok = False
            break
    c+=1

if ok:
    print('makes sense')
else:
    print('something is fishy')