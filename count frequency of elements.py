l=eval(input("Enter list: "))
l2=[]

for i in range(0,len(l)):
    count=0
    if l[i] not in l2:
        for j in range(i,len(l)):
            if l[i]==l[j]:
                count+=1
            
        print("no of occurrences of ",l[i]," in",l,"is:",count)
        l2.append(l[i])
