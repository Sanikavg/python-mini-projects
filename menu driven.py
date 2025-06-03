print("        MENU OPTIONS         ")
print("1. Sum of digits of a number")
print("2. Check Prime")
print("3. Count vowels in a string")
print("4. EXIT")
while True:
    ch=int(input("Enter your choice: "))
    if ch==1:
        print("PROGRAM1: Sum of digits of a number")
        sum=0
        num=int(input("enter the number: "))
  
        while num>0:
             digit=num%10
             sum+=digit
             num=int(num/10)
        print("The sum of the digits of the numbers is ",sum)
        
    elif ch==2:
        print("PROGRAM2: Check Prime")
        num = int(input("Enter a number: "))  
  
        if num > 1:  
              for i in range(2,num//2+1):  
                 if (num % i) == 0:  
                    print(num,"is not a prime number")  
                    break  
              else:  
                 print(num,"is a prime number")  
         
        else:  
           print(num,"is not a prime number")

    elif ch==3:
         print("PROGRAM3: Count vowels in a string")
         a=(input("Enter a string: "))
         count=0
         for i in a:
             if i in 'aeiouAEIOU':
                 count+=1
         else:
             print("Count of vowels in ",a,"is ",count)
    elif ch==4:
         break

    else:
         print("INVALID CHOICE")
             
         


        
