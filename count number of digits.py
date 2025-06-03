num=int(input("Enter a number: "))
even=odd=0
while num>0:
          digit=num%10
          num=int(num/10)
          if digit%2==0:
                even+=1
          else:
                odd+=1
print("the even number of digits are: ",even)
print("the odd number of digits are: ",odd)
