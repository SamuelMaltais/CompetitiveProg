n = int(input())

for _ in range(n):
    start = 1
    line = input().split()
    size = int(line[0])
    start = int(line[1])

    for i in range(2, size):
        shouldBe = start + 1
        if int(line[i]) != shouldBe:
            print(i)
            break
        start = shouldBe