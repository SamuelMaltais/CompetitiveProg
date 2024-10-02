n = int(input())

def find(current, restant, operations, target):
    if restant == 0:
        return
    
    if restant == 2 and target - current == 1:
        operations.append("+")
        operations.append("/")
        return

    if current > target:
        pass
    


for _ in range(n):
    i = int(input())
    operations = []
    find(4, 3, operations, i)


