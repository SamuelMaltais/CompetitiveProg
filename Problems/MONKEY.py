line = input().split()
n = int(line[0])
k = int(line[1])

class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.n = 0
        self.left = None
        self.right = None

arr = [0 for _ in range(n + 1)]

def increment(tree, val):
    if tree == None:
        return
    tree.n += val
    increment(tree.right, val)
    increment(tree.left, val)


def change(tree, key, val, count):
    if key == tree.key:
        tree.n += val
        increment(tree.right, val)
    elif key > tree.key:
        if tree.right == None:
            tree.right = Node(key)
            tree.right.n += val + tree.n
        else:
            change(tree.right, key, val, tree.right.n)
    else:
        if tree.left == None:
            tree.left = Node(key)
            tree.left.n += val + count
        else:
            tree.n += val
            increment(tree.right, val)
            change(tree.left, key, val, count)

def lookup(tree, key, last):

    if tree == None:
        return last

    if key == tree.key:
        return tree.n
    elif key < tree.key:
        if tree.left == None:
            return last
        else:
            return lookup(tree.left, key, last)
    else:
        last = tree.n
        if tree.right == None:
            return last
        else:
            return lookup(tree.right, key, last)

tree = None

for _ in range(k):
    line = input().split()

    i = int(line[1])

    if line[0] == 'F':

        val = 1
        if arr[i] == 1:
            val = -1
            arr[i] = 0
        else:
            arr[i] = 1

        if tree == None:
            tree = Node(i)
            tree.n += 1
        else:  
            change(tree, i, val, 0)
    else:
        j = int(line[2])
        a = lookup(tree, i, 0)
        b = lookup(tree, j, 0)
        print(b - a + arr[i])

