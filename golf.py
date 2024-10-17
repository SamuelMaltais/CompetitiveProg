line = input().split()
while line != ['1','2','3','4','5']:
    for i in range(4):
        if(line[i] > line[i + 1]):
            temp = line[i]
            line[i] = line[i + 1]
            line[i + 1] = temp
            print(" ".join(line))