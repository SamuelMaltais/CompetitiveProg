for _ in range(int(input())):
    input()
    line1 = input()
    line2 = input()

    line1_offset1 = 0
    line1_offset2 = 0
    line2_offset1 = 0
    line2_offset2 = 0
    for i in range(0, len(line1), 2):
        if line1[i] == '0':
            line1_offset1 += 1
        if line2[i] == '0':
            line2_offset1 += 1
    for i in range(1, len(line1), 2):
        if line1[i] == '0':
            line1_offset2 += 1
        if line2[i] == '0':
            line2_offset2 += 1

    if line1_offset1 + line2_offset2 >= len(line1) / 2 and line1_offset2 + line2_offset1 >= len(line1) // 2:
        print('YES')
    else:
        print('NO')