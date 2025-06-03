l=[]
sum=0
count=0
num=int(input("enter the range of the list"))
print("enter the numbers")
for i in range(0,num):
    n=int(input())
    l.append(n)
large=max(l)
element=int(input("enter the element to be searched"))
for i in range(len(l)):
    if l[i]==element:
        count=count+1
        l[i]=large
    
    

       
if count==0:
    print("SEARCH UNSUCCESSFUL")
    for i in range(len(l)):
                 sum=sum+l[i]
    print("sum of all numbers is", sum)
 
else:
    print(l[i])
