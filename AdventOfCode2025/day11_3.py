import sys
import pulp
import numpy as np

sys.setrecursionlimit(999999999)


# Code copie de gpt, je suis un sellout
def solve_ilp(A, b, nonneg=True):
    """
    Solve: minimize sum(x_i) subject to A x = b and x integer.
    A: 2D numpy array of shape (m, n)
    b: 1D numpy array of shape (m,)
    """
    m, n = A.shape

    # Create problem
    prob = pulp.LpProblem("LargeILP", pulp.LpMinimize)

    # Create integer variables x_0, x_1, ..., x_(n-1)
    if nonneg:
        xs = [pulp.LpVariable(f"x_{i}", lowBound=0, cat="Integer") for i in range(n)]
    else:
        xs = [pulp.LpVariable(f"x_{i}", lowBound=None, cat="Integer") for i in range(n)]

    # Objective: minimize sum(x_i)
    prob += pulp.lpSum(xs)

    # Constraints: A · x = b
    for row in range(m):
        prob += pulp.lpSum(A[row, col] * xs[col] for col in range(n)) == b[row]

    # Solve
    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    # Extract solution
    solution = np.array([v.value() for v in xs], dtype=float)
    status = pulp.LpStatus[prob.status]

    return status, solution, pulp.value(prob.objective)

l= []

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        l.append(line.strip())

tot = 0
for line in l:
    line = line.split()
    buttons = line[1:len(line)-1]
    state = line[0][1:len(line[0]) - 1]
    end = list(map(int, line[-1][1:len(line[-1]) - 1].split(',')))
    
    totMoves = []
    for b in buttons:
        s = b[1:len(b) - 1]

        row = [0 for _ in range(len(end))]
        for i in list(map(int,s.split(","))):
            row[i] = 1

        totMoves.append(row)

    seen = {}
    ini = tuple([0 for _ in range(len(end))])
    
    arr = np.array(totMoves)
    b = np.array(end)

    arr = arr.transpose()
    a, b , c = solve_ilp(arr, b)
    tot += c

print(tot)


