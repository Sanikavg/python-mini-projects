
while True:
    l=eval(input("enter list: "))
    if len(l)%2==0:
        
      for i in range(0,len(l),2):
        l[i],l[i+1]=l[i+1],l[i]
          
      print("The swapped list is ",l)
      break
    else:
       print("Enter even number of elements")
       continue 
