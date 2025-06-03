import math
import random

print('''Menu
a) Input a number and display absolute value of a number.
b) Input a number and display square root of a number.
c) Generate a random number between 0 and 1.
d) Generate a negative random number between -100 and -50.''')

while True:
    c=int(input("Enter choice: "))
    if c==1:
        num=float(input("enter number: "))
        print(math.fabs(num))
    elif c==2:
        num=float(input("enter number: "))
        print(math.sqrt(num))
    elif c==3:
        print(random.random())
    elif c==4:
        print(random.randint(-100,-50))
    a=input("do you wish to continue(y/n): ")
    if a=='n':
        break
