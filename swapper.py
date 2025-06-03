
l=[]
n=int(input("Enter number of elements: "))
print("Enter the elements: ")
for i in range(n):
    a=int(input())
    l.append(a)

print("List is: ",l)

def swapper(l):
    len_l=len(l)
    if len_l%2!=0:
        len_l-=1
    for i in range(0,len_l,2):
        l[i],l[i+1]=l[i+1],l[i]
    return l

print("List after swapping :",swapper(l))
