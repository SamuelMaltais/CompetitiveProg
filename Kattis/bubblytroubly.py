glasses = []
levels = {}
possible_levels=[]
for _ in range(int(input())):
    x,y,z,r,v = list(map(int, input().split()))
    if z in levels:
        levels[z].append((x,y,r,v))
    else:
        possible_levels.append(z)
        levels[z] = [(x,y,r,v)]


possible_levels.sort()

max_t=0

# nb_enfants, temps avant de overfill, qte a donner apres overfill
outputs = {}

for i in reversed(range(possible_levels)):
    pass