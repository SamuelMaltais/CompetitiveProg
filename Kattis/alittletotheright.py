n, p = input().split()
s=set()
a=[]
for i in range(int(n)):
 a.append(tuple(map(int,(input().split()))))
def f(i,a):
 c=set()
 for e in a:
  if e[i] in c:
   return False
  c.add(e[i])
 return True
for i in range(len(a[0])):
 a.sort(key=lambda k:k[i])
 if f(i,a):
  s.add(tuple(a))
print(len(s))