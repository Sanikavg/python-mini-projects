l=eval(input("enter list: "))
for i in range(0,len(l)):
    if l[i]>0:
        l[i]=1
    elif l[i]<0:
        l[i]=-1
    else:
        l[i]=0
print("The new list is ",l)
