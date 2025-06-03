n=int(input("enter number: "))
even=odd=0
for i in str(n):
    if int(i)%2==0:
        even+=1
    else:
        odd+=1
print(even,odd)
