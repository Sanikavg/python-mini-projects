num=int(input("Enter a number: "))
sum=0
temp=num
ln=len(str(num))
while (num>0):
    value=num%10
    sum=sum+value**ln
    num=num//10

if sum==temp:
    print(temp," is an armstrong number")
else: 
    print(temp," is not an armstrong number")
