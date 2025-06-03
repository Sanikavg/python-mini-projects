s=input("Enter string: ")
d={}
for i in s.lower():
    if i==' ':
        continue
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print("characters","\t","frequency")
for i in d:
    print(i,"\t \t",d[i])
