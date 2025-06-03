def perfect(n):
    sum1=0
    for i in range(1,n):
        if n%i==0:
            sum1+=i
    return sum1==n

def palindrome(n):
    rev=0
    temp=n
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=int(n/10)
    if temp==rev:
        print(temp, "is a palindrome")
    else:
        print(temp, "is not a palindrome")

def armstrong(n):
    sum1=0
    temp=n
    p=len(str(n))
    while n>0:
        digit=n%10
        sum1+=digit**p
        n=int(n/10)
    if temp==sum1:
        print(temp,"is an armstrong number")
    else:
        print(temp,"is not an armstrong number")

def is_Prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
                break
        else:
            return True
    else:
        return False

def automorphic(n):
    x=n*n
    c=0
    while n>0:
        if (n%10)!=(x%10):
            c=1
            break
        n=n//10
        x=x//10
    return c==0
    
print("\t\t NUMBER CHECKER MENU")
print('''1) check whether a number is perfect or not.
2) check whether a number is palindrome or not.
3) check whether a number is armstrong no or not.
4) check whether a number is prime or not.
5) check whether a number is an automorphic number.
6) Exit''')
print()
while True:
    c=int(input("Enter choice number: "))
    print()
    if c==1:
        n=int(input("Enter number: "))
        print(perfect(n))
        print()
    if c==2:
        n=int(input("Enter number: "))
        palindrome(n)
        print()
    if c==3:
        n=int(input("Enter number: "))
        armstrong(n)
        print()
    if c==4:
        n=int(input("Enter number: "))
        print(is_Prime(n))
        print()
    if c==5:
        n=int(input("Enter number: "))
        print(automorphic(n))
        print()
    if c==6:
        print("Exit program...")
        break
    
    
    


        
        
        
        
            
            
