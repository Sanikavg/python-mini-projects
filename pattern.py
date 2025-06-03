#n=int(input("enter the number of rows: "))
for i in range (5,0,-1):
    for j in range (1,i+1):
        print(j,end=" ")
    print("\r")

for i in range (1,5+1):
    for j in range (1,i+1):
        print(j,end=" ")
    print("\r")
