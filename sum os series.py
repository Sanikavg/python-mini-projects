i=1
sum=0
n=int(input("enter the number of terms: "))
a=1
while n>0:
    sum+=i
    a+=1
    i+=a
    n-=1
print(sum)
