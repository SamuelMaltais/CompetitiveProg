class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def update(self, node, start, end, l, r, value):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0

        if start > r or end < l:
            return

        if start >= l and end <= r:
            self.tree[node] += (end - start + 1) * value
            if start != end:
                self.lazy[2 * node] += value
                self.lazy[2 * node + 1] += value
            return

        mid = (start + end) // 2
        self.update(2 * node, start, mid, l, r, value)
        self.update(2 * node + 1, mid + 1, end, l, r, value)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, l, r):
        if start > r or end < l:
            return 0

        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0

        if start >= l and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        left_sum = self.query(2 * node, start, mid, l, r)
        right_sum = self.query(2 * node + 1, mid + 1, end, l, r)
        return left_sum + right_sum

# Input handling and operations
line = input().split()
n = int(line[0])  # Number of elements
k = int(line[1])  # Number of operations

# Initialize the segment tree and bit states
segment_tree = SegmentTree(n)
arr = [0] * (n + 1)  # Track the state of each bit (0 or 1)

for _ in range(k):
    line = input().split()
    command = line[0]
    i = int(line[1])

    if command == 'F':  # Flip the bit
        if arr[i] == 0:  # Currently 0, flip to 1
            segment_tree.update(1, 1, n, i, i, 1)
            arr[i] = 1
        else:  # Currently 1, flip to 0
            segment_tree.update(1, 1, n, i, i, -1)
            arr[i] = 0
    elif command == 'C':  # Query range sum
        j = int(line[2])
        result = segment_tree.query(1, 1, n, i, j)
        print(result)
