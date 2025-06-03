num=int(input("enter the number: "))

if num%2==0:
    for i in range(2,num+1,2):
        print(i,end=" ")
        
elif num%2!=0:
      for i in range(1,num+1,2):
        print(i,end=" ")
