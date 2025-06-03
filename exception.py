'''a=int(input("Enter a: "))
b=int(input("Enter b: "))
print(a/b)
print("hi")'''

try:
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    c=a/b
    int("4")
    print(a/b)
except Exception as e:       #e is object of the exception class
    #print("can't divide by zero")
    print(e)

#print("hi")
else: 
    d=20
    print(c+d)
finally:
    print("hello")


'''except ValueError:
    print("Value inappropriate")

except TypeError:

    print("can't divide by zero")'''
