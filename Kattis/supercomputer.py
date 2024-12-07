line = input().split()
n = int(line[0])
k = int(line[1])

class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.n = 0
        self.left = None
        self.right = None

arr = [0 for _ in range(n)]

def change(tree, key, val, count):
    if key == tree.key:
        tree.n += val
    elif key > tree.key:
        if tree.right == None:
            tree.right = Node(key)
            tree.right.n += val + count
        else:
            change(tree.right, key, val, tree.right.n)
    else:
        change(tree.right, )

def travel(tree, key):
    pass
