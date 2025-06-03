l=[]
num=int(input("enter the range of the list"))
print("enter the numbers")
for i in range(0,num):
    n=int(input())
    l.append(n)
for i in range(len(l)):
    if l[i]%2==0:
        l[i]=l[i]/2
    else:
        l[i]=2*l[i]
print(l)
