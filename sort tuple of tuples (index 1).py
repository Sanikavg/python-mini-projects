T1 = (('a', 23),('b', 37),('c', 11), ('d',29))
l=list(T1)

for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j][1]>l[j+1][1]:
            l[j],l[j+1]=l[j+1],l[j]
        
print(tuple(l))

