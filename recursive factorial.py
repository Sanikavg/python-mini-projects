def factorial(n):
    global fact
    if n == 1:
        return fact
    return fact * n * factorial(n-1)


n= int(input("Enter number: "))
if n == 0:
    print("Factorial is 1 ")
else:
    fact = 1
    print("Factorial of ",n,":",factorial(n))

