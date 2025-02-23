# Read number of rooms and corridors
n, m = map(int, input().split())

# Read the corridors; store each as (u, v, index)
edges = []
for i in range(m):
    u, v = map(int, input().split())
    edges.append((u, v, i + 1))

# Partition edges based on the natural order (rooms numbered 1,2,...,n)
forward = []   # edges from a lower-numbered room to a higher-numbered room
backward = []  # edges from a higher-numbered room to a lower-numbered room

for u, v, idx in edges:
    if u < v:
        forward.append(idx)
    else:
        backward.append(idx)

# We choose to remove the smaller set of edges.
# If we remove the forward edges, then in the reverse ordering (n, n-1, ..., 1),
# the kept (backward) edges become forward, which is acyclic.
if len(forward) <= len(backward):
    removed = forward
else:
    removed = backward

# Output the number of corridors to remove and their indices.
print(len(removed))
for idx in removed:
    print(idx)
