line = input().split()

r = int(line[0])
s = int(line[1])
l = int(line[2])

ppl = {}
corp = {}
for i in range(1, r + 1):
    ppl[i] = 0

for i in range(1, s + 1):
    corp[i] = 0


for _ in range(l):
    line = input().split()
    person = int(line[0])
    corporation = int(line[1])

    if ppl[person] > corp[corporation]:
        corp[corporation] += 1
        print("CORP " + str(corporation))
    else:
        ppl[person] += 1
        print("INDV " + str(person))

print(corp)
print(ppl)