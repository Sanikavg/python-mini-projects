d1={}
n=int(input("enter number of data to be entered: "))
i=1
while i<=n:
    pro=input("Enter product name: ")
    price=float(input("Enter price: "))
    d1[pro]=price
    i+=1

while True:
    a=input("Enter product name: ")
    print(d1.get(a,'not available'))
    con=input("do you want to continue? (y/n): ")
    if con=='n':
        break
