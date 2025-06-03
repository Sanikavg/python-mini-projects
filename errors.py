try:
    a=int(input("enter a: "))
    c=int(input("enter c: "))
    
    if a<4:
        b=a/c

    print("the value of b = ",b)
except:
    print("error occurred and handled")
import sys
try:
    a=int(input())
except(ValueError):
    print("error")
    sys.exit()
    
print("hello")
