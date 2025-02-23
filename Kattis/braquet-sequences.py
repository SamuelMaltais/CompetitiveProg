import sys
sys.setrecursionlimit(9**9)
input()
l=input().split()
m=10**9+7
def c(d,i,v):
 if i>=len(l):
  return v,i
 if l[i]==')':
  return v,i
 if l[i]=='(':
  t,i=c(d+1,i+1,(d+1)%2)
 else:
  t=int(l[i])
 if d%2==0:
  return c(d,i+1,(v+t)%m)
 else:
  return c(d,i+1,(v*t)%m)
s,i=c(0,0,0)
print(s)