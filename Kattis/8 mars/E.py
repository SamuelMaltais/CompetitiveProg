cheese = 0
glory = 0

events = []
for _ in range(int(input())):
    event = input().split()
    events.append(event)

time = int(input())

for e in events:
    if int(e[1]) > time:
        continue
    if e[0] == "CAUGHT":
        cheese += int(e[1])
        glory += int(e[2])
    else:
        cheese -= int(e[1])
        glory -= int(e[2])

print(cheese, glory)
