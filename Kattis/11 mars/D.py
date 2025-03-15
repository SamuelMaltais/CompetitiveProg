arr = []
for i in range(int(input())):
    arr.append(input())

winner='a'
lead = -1
p1 = 0
p2 = 0
for elem in arr:
    if elem == 'Yraglac':
        p1 += 1
    else:
        p2 += 1
        
    if p1 > p2:
        curr_lead = p1 - p2
        if curr_lead == lead and winner == 'b':
            winner = 'c'
        elif curr_lead > lead:
            lead = curr_lead
            winner = 'a'
    if p1 < p2:
        curr_lead = p2 - p1
        if curr_lead == lead and winner == 'a':
            winner = 'c'
        elif curr_lead > lead:
            lead = curr_lead
            winner = 'b'
    
def count_consecutive(s, arr):
    curr=''
    tot = 0
    b=0
    for elem in arr:
        if elem == s:
           tot += 1
           b=max(tot, b)
        else:
            tot = 0
    return b

a = count_consecutive('Yraglac', arr)
b = count_consecutive('Notnomde', arr)
winner2 = 'a'
if b > a:
    winner2 = 'b'
elif b == a:
    winner2 = 'c'
    
    
if winner == winner2:
    print('Agree')
else:
    print("Disagree")