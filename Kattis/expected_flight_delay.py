import math

a,b,c,d = input().split()

iniday = int(a)
wday = int(b) / 100
wend = int(c) / 100
needed = int(d) / 100

p_echouer_semaine = (1 - wday)**5 * (1 - wend)**2
semaine_necessaire = 0

if p_echouer_semaine > 0:
    semaine_necessaire = math.log(1 - needed, p_echouer_semaine)


semaine_necessaire = math.floor(semaine_necessaire)

days = 7*semaine_necessaire
p_echec = p_echouer_semaine ** semaine_necessaire

curr_day = iniday - 1
if curr_day == 0:
     curr_day = 7

while p_echec > (1 - needed):
        if curr_day == 1 or curr_day == 7:
            p_echec *= (1-wend)
        else:
            p_echec *= (1-wday)

        days += 1
        curr_day -= 1
        if curr_day == 0:
            curr_day = 7

m = ['','Sunday', 'Monday','Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday']

if curr_day == 7:
      curr_day = 0

if days == 1:
    print('Try to leave on ' + m[(curr_day + 1) % 8] + ', ' + str(days) + ' day before the '+ m[iniday] + ' meeting.')
else:
    print('Try to leave on ' + m[(curr_day + 1) % 8] + ', ' + str(days) + ' days before the '+ m[iniday] + ' meeting.')
    