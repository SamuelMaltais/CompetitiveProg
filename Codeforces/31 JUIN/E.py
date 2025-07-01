def makeSeq(a, i, res):
    

    return i



for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    
    counts = [a.count(i) for i in range(max(a) + 2)]

    first_zero = counts.index(0)

    s=0
    psum=[]
    for c in counts:
        s+=c
        psum.append(s)

    enters = {}
    leaves = {}



    for i in range(len(counts)):
        if counts[i] != 0:
            if i < first_zero:

                time = psum[first_zero] - psum[i] + counts[i]
                enters[time] = enters.get(time, 0) + 1

                time = (psum[-1] - i) + 1
                leaves[time] = leaves.get(time, 0) + 1
            
            else:
                enters[i] = psum[i]
                leaves[time] = leaves.get(time, 0) + 1

                time = (psum[-1] - i) + 1
                leaves[time] = leaves.get(time, 0) + 1


    res = []
    
    answ = 0

    for i in range(n + 1):
        answ += enters.get(i, 0)
        answ -= leaves.get(i, 0)
        res.append(str(answ))
    print(" ".join(res))

        
