gold, silver, copper = list(map(int, input().split()))


tot = 3*gold + 2*silver + copper

c1 = ""
if tot >= 8:
    c1 = 'Province'
elif tot >= 5:
    c1 = 'Duchy'
elif tot >= 2:
    c1 = 'Estate'

c2 = ""
if tot >= 6:
    c2 = 'Gold'
elif tot >= 3:
    c2 = 'Silver'
else:
    c2 = 'Copper'

if c1 != "":
    print(c1 + ' or ' + c2)
else:
    print(c2)


