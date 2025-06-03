def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

def power(x,n):
    return x**(2*n)

n=int(input("Enter number(n): "))
x=int(input("Enter number(x): "))
series=0
for i in range(1,n+1):
    series+=power(x,i)/factorial(i)
print("Sum of series is: ",series)

    
    
