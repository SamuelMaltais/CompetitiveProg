class Node:
    def __init__(self, left_bound, right_bound, left_tree=None, right_tree=None, val=None):
        self.left = left_tree
        self.right = right_tree
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.val = val 


def merge_values(left_val, right_val):
    merged = {}
    for i in range(1, 7):
        merged[i] = left_val.get(i, 0) + right_val.get(i, 0)
    return merged

def make_tree(left, right, gems):

    if left == right:
        gem_count = {int(gems[left]): 1}
        return Node(left, right, None, None, gem_count)

    mid = (left + right) // 2
    left_child = make_tree(left, mid, gems)
    right_child = make_tree(mid + 1, right, gems)

    total = merge_values(left_child.val, right_child.val)

    return Node(left, right, left_child, right_child, total)

def update_tree(tree, i, prev, new):
    if tree.left_bound == tree.right_bound == i:
        tree.val[prev] = max(tree.val.get(prev, 0) - 1, 0)
        tree.val[new] = tree.val.get(new, 0) + 1
        return

    mid = (tree.left_bound + tree.right_bound) // 2
    if i <= mid and tree.left:
        update_tree(tree.left, i, prev, new)
    elif tree.right:
        update_tree(tree.right, i, prev, new)

    tree.val = merge_values(tree.left.val, tree.right.val)

def query_tree(tree, left, right):
    if tree.left_bound >= left and tree.right_bound <= right:
        return tree.val

    if tree.right_bound < left or tree.left_bound > right:
        return {}

    left_result = query_tree(tree.left, left, right) if tree.left else {}
    right_result = query_tree(tree.right, left, right) if tree.right else {}
    return merge_values(left_result, right_result)

vals = {}
line = input().split()
n = int(line[0])
q = int(line[1])

for i, val in zip(range(1, 7), input().split()):
    vals[i] = int(val)

gems = list(map(int, input().strip()))

tree = make_tree(0, len(gems) - 1, gems)


for _ in range(q):
    line = input().split()
    query_type = int(line[0])
    val1 = int(line[1])
    val2 = int(line[2])

    if query_type == 1:
        index = val1 - 1 
        prev_gem = gems[index]
        new_gem = val2
        gems[index] = new_gem
        update_tree(tree, index, prev_gem, new_gem)

    elif query_type == 2:

        vals[val1] = val2

    elif query_type == 3:

        left = val1 - 1  
        right = val2 - 1
        result = query_tree(tree, left, right)
        total = sum(vals[key] * count for key, count in result.items())
        print(total)
