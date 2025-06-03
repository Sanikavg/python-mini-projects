def integer(a):
    print("before increment: ",id(a))
    a+=5
    print("after increment: ",id(a))
a=float(input("enter number: "))
print("before function call: ",id(a))
integer(a)
