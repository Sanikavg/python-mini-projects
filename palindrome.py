num=int(input("Enter value of num: "))

rev=0
i=num
while(num>0):
     digit=num%10
     num=int(num/10)
     rev=(rev*10)+digit
if rev==i:
    print(i)

