import heapq
n=int(input())

curr_balance=0
positions = []
bestweights = []
m = {}

for i in range(n):
    p, w = input().split()
    p=int(p)
    w=int(w)
    curr_balance += p*w
    heapq.heappush(bestweights, (-w,w, p, 1))
    positions.append((p,w,1))
    m[p] = i

# Trick pour faire un mouvement 1 == on bouge a droite ou -1 bouge a gauche
direction = -1 if curr_balance > 0 else 1
curr_balance = abs(curr_balance)

total = 0



while curr_balance > 0:
    if len(bestweights) == 0:
        print("NOPE")
        break
    value, weights, position, people = heapq.heappop(bestweights)
    
    # print("Array index", m[position], positions)
    # print("position:",position, bestweights, curr_balance)
    # print("weights", weights)
    # print()

    i = m[position]
    # On deal avec une positions merged, elle ne devrait plus etre dans le heap
    if positions[i] == None or positions[i][1] != weights:
        continue
    # print(positions, bestweights)
    # On marque position comme None puisqu'on bouge tous les gens
    positions[i] = None
    i += direction
    
    max_possible_dist = float('infinity')
    new_index = 0

    while 0 <= i < len(positions):
        if positions[i] != None:
            max_possible_dist = abs(positions[i][0] - position)
            new_index = i
            break
        i += direction

    if weights == 0:
        print("impossible")
        break
    what_we_need = (curr_balance / weights)
    curr_balance -= min(what_we_need*weights, max_possible_dist*weights)

    # print("max-dist", max_possible_dist, curr_balance)
    travaled = min(what_we_need, max_possible_dist) * people
    total += travaled

    if curr_balance > 0:
        if new_index >= len(positions) or new_index < 0:
            print("impossible")
            break
        if positions[new_index] == None:
            break
        # Apres on merge la case ou nous sommes arrives
        weights += positions[new_index][1]
        people += positions[new_index][2]
        value = weights / people
        new_position = positions[new_index][0]
        positions[new_index] = (new_position, weights, people)   
        heapq.heappush(bestweights, (-value, weights, new_position, people))

formatted_number = f"{total:.6f}" 
print(formatted_number)

