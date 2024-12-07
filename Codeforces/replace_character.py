res = []
for _ in range(int(input())):
    input()
    s = list(input())
    maj = {}
    for c in s:
        maj[c] = maj.get(c,0) + 1
    
    curr_best_target = 0
    target_letter = ""
    best_initial = 9999999999
    target_initial = None

    for r in range(1, len(s) + 1):
        i = len(s) - r
        c = s[i]
        if maj[c] > curr_best_target:
            curr_best_target = maj[c]
            target_letter = c
        if maj[c] < best_initial:
            best_initial = maj[c]
            target_initial = i
        elif maj[c] == best_initial and c != target_letter:
            target_initial = i
        
    s[target_initial] = target_letter
    res.append("".join(s))
print('\n'.join(res))     