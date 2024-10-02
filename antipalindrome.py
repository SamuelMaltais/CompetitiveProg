line = input().replace(" ", "")
line = line.lower()
line = line.replace(".", "")
line = line.replace(",", "")
line = line.replace("-", "")
line = line.replace("_", "")
line = line.replace("'", "")


flag = True
for i in range(len(line)):
    if i > 0 and i < len(line) - 1:
        if line[i - 1] == line[i + 1]:
            print("Palindrome")
            flag = False
            break
    if i < len(line) - 1:
        if line[i] == line[i + 1]:
            print("Palindrome")
            flag = False
            break

if flag:
    print("Anti-palindrome")


    
