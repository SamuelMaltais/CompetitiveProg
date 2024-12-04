n = int(input())

line = input().split()

p = []

for i in range(len(line)):
    p.append([int(line[i]), i, False])

p.sort(key=lambda x: x[0])

final_arr = []


for i in range(len(p)):
    removed = 0
    for j in range(1, len(p) - i):
        if p[j][2] == True:
            continue

        if p[i][1] > p[j][1]:
            final_arr.append(p[j])  
            p[j][2] = True 
            removed += 1
            final_arr

            if removed == 1:
                final_arr.append(p[i])
                p[i][2] = True
            else:
                continue
            

for elem in p:
    if elem[2] == False:
        final_arr.append(elem)


total = 0
for i in range(1, len(final_arr)):
    if final_arr[i][1] > final_arr[i - 1][1]:
        total += final_arr[i][0]
    else:
        total += final_arr[i - 1][0]

print(total)