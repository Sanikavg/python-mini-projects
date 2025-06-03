num=int(input("enter the number: "))

value=0
while(num>0):
     reverse=num%10
     value=reverse+(value*10)
     num=num//10

print("the reverse value is", value)
