a, count = list(map(int, input().split()))
arr = list(input())

def backtrack(arr, count):
    if count == 0:
        return True
    for i in range(len(arr) - 1):
        left = arr[i]
        right = arr[i + 1]
        if left != 'R' and right != 'L':
            arr_cpy = arr[:]
            arr_cpy[i] = 'R'
            arr_cpy[i + 1] = 'L'
            if backtrack(arr_cpy, count - 1):
                return True
    
    return False

print(int(backtrack(arr, count)))