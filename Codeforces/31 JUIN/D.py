


# 

# 001000

for _ in range(int(input())):
    n, k = input().split()
    line = input()
    k = int(k)
    if k >= line.count('1'):
        print("Alice")
        continue
    if k <= (len(line) // 2):
        print('Bob')
    else:
        print('Alice')
    

    
