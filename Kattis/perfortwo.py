m=[[[3,1],[5,2]],[[6,3],[8,4]],[[7,4],[9,5]],[[0,1],[5,4],[10,6],[12,7]],[[11,7],[13,8]],[[0,2],[3,4],[12,8],[14,9]],[[1,3],[8,7]],[[2,4],[9,8]],[[1,4],[6,7]],[[2,5],[7,8]],[[3,6],[12,11]],[[4,7],[13,12]],[[3,7],[5,8],[10,11],[14,13]],[[4,8],[11,12]],[[5,9],[12,13]]]
def f(pos):
    best=1500000
    mo=[]
    for i1,i2 in enumerate(pos.copy()):
        if (i2==0):
            for j in m[i1]:
                if (pos[j[0]]!=0 and pos[j[1]]!=0):
                    mem0=pos[j[0]]
                    mem1=pos[j[1]]
                    pos[i1]=mem0
                    pos[j[0]]=0
                    pos[j[1]]=0
                    val=f(pos)+mem1*mem0
                    if(val>best or best==1500000):
                        best=val
                    pos[i1]=0
                    pos[j[0]]=mem0
                    pos[j[1]]=mem1
    if(best==1500000):
        return 0
    else:
        return -best
p=list(map(int,(input()+" "+input()+" "+input()+" "+input()+" "+input()).split()))
print(-f(p))