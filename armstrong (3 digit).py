num=int(input("Enter a three digit number: "))
sum=0
temp=num

while (num>0):
    value=num%10
    sum=sum+value**3
    num=num//10

if sum==temp:
    print(temp," is an armstrong number")
else: 
    print(temp," is not an armstrong number")
