import math

a,b,c,d = input().split()

iniday = int(a)
wday = int(b) / 100
wend = int(c) / 100
needed = int(d) / 100

days = 0

curr_day = iniday - 1
if curr_day == 0:
        curr_day = 7

odds = 0
days = 0

while odds < needed:
        if curr_day == 1 or curr_day == 7:
            odds += wend*(1-odds)
        else:
            odds += wday*(1-odds)

        days += 1
        curr_day -= 1
        if curr_day == 0:
            curr_day = 7


m = ['','Sunday', 'Monday','Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday']

if curr_day == 7:
     curr_day = 0

if days == 1:
    print('Try to leave on ' + m[curr_day + 1] + ', ' + str(days) + ' day before the '+ m[iniday] + ' meeting.')
else:
    print('Try to leave on ' + m[curr_day + 1] + ', ' + str(days) + ' days before the '+ m[iniday] + ' meeting.')
    