def insertion_sort(L):
    for K in range(1,len(L)):
        temp = L[K]
        ptr = K-1
        while (ptr>=0) and (L[ptr]<temp):
                           L[ptr+1]=L[ptr]
                           ptr = ptr-1
        L[ptr+1]=temp
    return L

L=eval(input("Enter element to be list: "))
L= insertion_sort(L)
print("List after sorting: ",L) 
                        
