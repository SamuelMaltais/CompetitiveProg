# Taken represents wich indicies have been taken in the current branch of recursion
def createPermutations(initial_string, taken, current):
    if len(current) == len(initial_string):
        return [current]
    

    # We recursively pick from the availiable letters, in order of availiablilty
    valid_permutations = []
    for i in range(len(taken)):
        if not taken[i]:
            new_taken = taken[:]
            new_taken[i] = True
            new_strings = createPermutations(initial_string, new_taken, current + initial_string[i])
            valid_permutations = valid_permutations + new_strings

    return valid_permutations

initial_string = input()

permutations = createPermutations(initial_string, [False for i in range(len(initial_string))], "")

# Removes duplicates
permutations = list(set(permutations))
print(permutations)