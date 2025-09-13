m={
    "upper": "3",
    "middle": "2",
    "lower": "1"
}
def c(s):
    v=s.split()
    a=v[1].split("-")
    num = "0."
    for e in reversed(a):
        num += m[e]

    return (float(num),v[0][:-1])

for _ in range(int(input())):
    l=[]
    for _ in range(int(input())):
        l.append(c(input()))

    l.sort(key=lambda e: (e[0], -ord(e[1])))
    for elem in l:
        print(elem[1])
    
    print("="*30)


