import math

def compute_derangement(N):
    # Base cases
    if N == 0:
        return 1
    elif N == 1:
        return 0
    elif N == 2:
        return 1
    
    # Dynamic programming for derangements
    D = [0] * (N + 1)
    D[0] = 1
    D[1] = 0
    D[2] = 1
    
    for i in range(3, N + 1):
        D[i] = (i - 1) * (D[i - 1] + D[i - 2])
    
    return D[N]

def probability(N):
    # Total permutations is N!
    total_permutations = math.factorial(N)
    
    # Derangements
    D_N = compute_derangement(N)
    
    # Probability that at least one person draws their own name
    prob = 1 - (D_N / total_permutations)
    
    return prob

# Read the number of citizens
N = int(input().strip())


if N < 15:
    result = probability(N)
else:
    result = 1 - (1 / math.e)

# Print the result with the required precision
print(result)
