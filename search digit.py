num=int(input("enter a number: "))
digit=int(input("enter the digit to search: "))
present=0
i=num
while num>0:
    if (num%10)==digit:
           present+=1
           num=int(num/10)
    else:
       num=int(num/10)
if present>0:
    print("The digit ",digit, "is present in", i)
else:
    print("The digit ",digit, "is not present in", i)

