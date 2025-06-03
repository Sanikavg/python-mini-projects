l=eval(input("Enter list: "))
i=0
n=len(l)
while i<n:
    if l[i]==0:
        for j in range(i,n-1):
            l[j]=l[j+1]
        l[n-1]=0   
        n-=1
    else:
        i+=1
print("modified list: ",l)

    
