def f():
 return list(map(int,input().split()))
f()
a=f()
b=sorted(f(),reverse=True)
s=0
o=0
for i in range(len(a)):
 s+=b[i];o=max(o,(a[i]+s)/(i+1))
print(o)