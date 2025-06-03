num=int(input("enter the end limit: "))

product=1
if num>0:
   for i in range(1,num+1):
        product=product*i
        
   print(product)
else:
    print("the number has to be greater than 0")

