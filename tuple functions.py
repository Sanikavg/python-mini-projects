t=(1,2,3)
t2=(3,4,5)
#comparing tuples: check if each element is greater 
res=all(x<y for x,y in zip(t,t2))
print(str(res))
print(len(t))
print(max(t))
print(min(t))
#comparing tuples
if t>t2:
    print(t,"is bigger")
else:
    print(t2,"is bigger")

      
