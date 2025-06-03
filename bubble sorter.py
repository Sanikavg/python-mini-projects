l=[]
n=int(input("Enter number of elements: "))
print("Enter the elements: ")
for i in range(n):
    a=int(input())
    l.append(a)

print("List is: ",l)

def bubblesort(l):
    for i in range(len(l)):
        for j in range(0,(len(l)-1)-i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l

print("Sorted list: ",bubblesort(l))
                
