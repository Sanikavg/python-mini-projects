def bubble_sort(L):
    for i in range(len(L)):
        for j in range(0,len(L)-i-1):
            if L[j] > L[j+1]:
                temp = L[j+1]
                L[j+1] = L[j]
                L[j] = temp
    return L
L=eval(input("Enter element to be list: "))
L= bubble_sort(L)
print("List after sorting: ",L) 
