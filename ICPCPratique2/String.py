import sys

def isLegit(start, word, pattern):

    for char in pattern:
        if start >= len(word):
            return False
        if word[start] != char:
            return False
        start += 1
    return True



patterns = []
lines = []
i = 0
for line in sys.stdin:
    if i % 2 == 0:
        patterns.append(line.strip())
    else:
        lines.append(line.strip())
    i += 1

res = []

for i in range(len(lines)):
    curr_pos = 0
    pattern = patterns[i]
    s = lines[i]

    pattern = list(pattern)
    s = list(s)

    awns = []

    for i in range(len(s)):
        if isLegit(i, s, pattern):
            awns.append(str(i))

    res.append(" ".join(awns))

print("\n".join(res))