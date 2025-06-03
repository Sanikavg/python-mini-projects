

num2=int(input("enter the ending range: "))
num2=num2+1
for i in range(2,num2):
      if i==2 or i==3:
          print(i, "is a prime number")

      elif i%2==0 or i%3==0:
            print(i, "is not a prime number")
      elif i%2!=0 and i%3!=0:
            print(i," is a prime number")
      else:
            print(i, "is neither prime nor composite")
    
