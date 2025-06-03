l=[]
largest=0
print("enter the numbers")
for i in range(0,10):
    n=int(input())
    l.append(n)
'''for i in range(len(l)):
    if l[i]>largest:
        largest=l[i]'''
print(max(l))
