items = []

def bruteforce(items, i, current_sour, current_bitter):
    if i == len(items):
        return abs(current_bitter - current_sour)
    
    exclude = bruteforce(items, i + 1, current_sour, current_bitter)
    current_sour = current_sour * int(items[i][0])
    current_bitter += int(items[i][1])
    other = bruteforce(items, i + 1, current_sour, current_bitter)
        
    return min(exclude, other)

for i in range(int(input())):
    items.append(input().split())


sol = -1
for i in range(len(items)):
    current_sour = int(items[i][0])
    curr = bruteforce(items, i + 1, current_sour, int(items[i][1]))
    if sol == -1:
        sol = curr
    else:
        sol = min(curr, sol)
    
print(sol)