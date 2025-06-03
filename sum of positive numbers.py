i=1
sum=0
while i>0:
  num=int(input("enter the number: "))
  
  if num<=0:
      print("The program is only for positive numbers")
      print("The sum of the numbers is ",sum)
      break
  sum+=num
  
