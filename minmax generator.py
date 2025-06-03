def largest(t):
    l=0
    for i in t:
        if i>l:
            l=i
    return l
        
def smallest(t):
    s=t[0]
    for i in t:
        if i<s:
            s=i
    return s
t=()
n=int(input("Enter number of elements: "))
print("Enter elements: ")
for i in range(n):
    a=int(input())
    t+=(a,)
print("Tuple is: ",t)
print("Largest element in tuple: ",largest(t))
print("Smallest element in tuple: ",smallest(t))
    
    
