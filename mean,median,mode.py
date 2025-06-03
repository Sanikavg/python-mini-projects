l=eval(input("Enter list: "))
print("Mean: ",sum(l)/len(l))
mostcount=0
for i in l:
    if l.count(i)>mostcount:
        mode=i
        mostcount=l.count(i)
if l.count(mode)==1:
    print("Mode: All elements occur only once. No element is repeated")
else:
    print("mode: ",mode)
l.sort()
if len(l)%2==0:
    median=(l[(len(l)//2)-1]+l[(len(l)//2)])/2
    print("Median: ",median)
else:
    median=l[((len(l)+1)//2)-1]
    print("Median: ",median)

