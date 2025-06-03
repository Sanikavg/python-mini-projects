t=int(input())
n,k=map(int,input().split())
l=[]
a=input()
for i in a:
    if i!=' ':
      l.append(int(i))

for i in range(k):
        x=l.pop(len(l)-1)
        l.insert(0,x)

s=' '
for i in l:
    s+=str(i)+' '
print(s)
        
    

