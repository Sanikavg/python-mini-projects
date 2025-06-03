num=int(input("enter the number: "))
rev=0
i=num
while(num>0):
     digit=num%10
     num=int(num/10)
     rev=(rev*10)+digit
     
print("The reverse of",i,"is",rev)
