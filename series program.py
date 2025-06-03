i=1
sum=value=0
b=0
n=int(input("enter the number of terms: "))
a=1
while n>1:
    sum+=i
    i+=2
    b=sum+i
    n-=1
    value=b+sum+1
print(value)
'''while i<=n:
    j=1
    while j<=(i+1):
        sum+=j
        j+=2
        
    i+=1
print(sum)'''





