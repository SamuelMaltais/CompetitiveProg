for _ in range(int(input())):
    a = input()
    b = input()
    sa = str(a)
    sb = str(b)
    lexo_bigger = (sa > sb)
    bigger = False

    if len(sa) > len(sb):
        bigger = True
    elif len(sa) == len(sb):
        for i in range(len(sa)):
            if sa[i].isupper() and sb[i].islower():
                bigger = True
                